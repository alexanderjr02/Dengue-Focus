from flask import Flask, render_template
from flask_socketio import SocketIO
import boto3
import base64
import os
import uuid  # hash da imagem -> id único
from stt_api import transcribe_audio  # Importando a função da API STT
import json
from tts import get_audio_url_from_tts  # Importar a função de TTS

app = Flask(__name__)  # A pasta 'templates' padrão será usada
socketio = SocketIO(app)

# Configurações da AWS
aws_region = "us-east-1"  # Altere conforme necessário
s3_bucket = "denguefoto"

# Inicialização dos clientes da AWS
lex_client = boto3.client("lexv2-runtime", region_name=aws_region)
s3_client = boto3.client("s3", region_name=aws_region)

# Variáveis do bot Lex V2 (alterar conforme necessário)
bot_id = "XLBAZBBYLD"
bot_alias_id = "QWV0WA4M8N"
locale_id = "pt_BR"


@app.route("/")
def index():
    return render_template("index.html")  # O template está na pasta 'templates'


@socketio.on("send_message")
def handle_message(data):
    user_message = data["message"]
    session_id = data.get("user_id", "user123")  # Usar o user_id do data ou 'user123'

    try:
        # Enviar a mensagem para o Amazon Lex V2
        response = lex_client.recognize_text(
            botId=bot_id,
            botAliasId=bot_alias_id,
            localeId=locale_id,
            sessionId=session_id,
            text=user_message,
        )

        print(f"Resposta completa do Lex: {response}")  # Log para depuração

        # Verificar se a resposta contém mensagens
        if "messages" in response and response["messages"]:
            for msg in response["messages"]:
                print(f"Mensagem do Lex: {msg}")

                # Processar mensagens do tipo PlainText
                if msg.get("contentType") == "PlainText" and "content" in msg:
                    audio_url = get_audio_url_from_tts(msg["content"])
                    print(f"Mensagem do Lex: {msg['content']}")
                    print(f"URL do áudio gerado: {audio_url}")

                    socketio.emit(
                        "receive_message",
                        {"message": msg["content"], "audioUrl": audio_url},
                    )

                # Processar mensagens do tipo ImageResponseCard
                elif msg.get("contentType") == "ImageResponseCard":
                    card = msg["imageResponseCard"]
                    buttons = card.get("buttons", [])
                    socketio.emit(
                        "receive_card", {"title": card["title"], "buttons": buttons}
                    )
        else:
            # Caso de fallback: tratar explicitamente
            print("Nenhuma mensagem válida encontrada na resposta do Lex.")
            handle_fallback()

    except Exception as e:
        error_message = str(e)  # Capturar a mensagem de erro
        socketio.emit(
            "receive_message",
            {"message": f"Erro ao se comunicar com o bot: {error_message}"},
        )
        print(f"Erro: {error_message}")  # Log do erro no console


def handle_fallback():
    """
    Função para tratar manualmente o fallback.
    """
    fallback_message = "Desculpe, não entendi o que você disse. Mas podemos te ajudar com as seguintes funções:"
    card_response = {
        "title": "Como posso te ajudar?",
        "buttons": [
            {
                "text": "Análise de Foco por Imagem",
                "value": "Análise de foco por imagem",
            },
            {"text": "Verificar Sintomas", "value": "Sintomas"},
            {"text": "Dicas de Prevenção", "value": "Prevenção"},
            {"text": "Dicas de Tratamento", "value": "Tratamento"},
            {"text": "Informação para Contato", "value": "Informação para contato"},
        ],
    }

    # Emitir mensagem e card para o front-end
    socketio.emit("receive_message", {"message": fallback_message})
    socketio.emit("receive_card", card_response)


@socketio.on("send_audio")
def handle_audio(data):
    audio_data = data["audio"].split(",")[1]
    audio_bytes = base64.b64decode(audio_data)

    # Salvar áudio no S3
    audio_file_name = "audio/user_audio.mp3"
    s3_client.put_object(Bucket=s3_bucket, Key=audio_file_name, Body=audio_bytes)

    # Chamar a função de transcrição
    try:
        audio_content_base64 = base64.b64encode(audio_bytes).decode("utf-8")
        transcription_result = transcribe_audio(audio_content_base64)
        transcript_text = json.loads(transcription_result["body"])["transcript"]

        print(f"Texto transcrito: {transcript_text}")

        # Enviar a transcrição para o Lex
        response = lex_client.recognize_text(
            botId=bot_id,
            botAliasId=bot_alias_id,
            localeId=locale_id,
            sessionId="user123",
            text=transcript_text,
        )

        print(f"Resposta do Lex: {response}")

        # Verificar resposta do Lex e enviar ao frontend
        if "messages" in response and response["messages"]:
            for msg in response["messages"]:
                if "content" in msg:
                    socketio.emit("receive_message", {"message": msg["content"]})

                # Verificar se é um response card
                if "contentType" in msg and msg["contentType"] == "ImageResponseCard":
                    card = msg["imageResponseCard"]
                    buttons = card.get("buttons", [])
                    socketio.emit(
                        "receive_card", {"title": card["title"], "buttons": buttons}
                    )
        else:
            # Caso de fallback
            handle_fallback()

    except Exception as e:
        error_message = str(e)
        socketio.emit(
            "receive_message",
            {"message": f"Erro ao processar a transcrição: {error_message}"},
        )


@socketio.on("send_image")
def handle_image(data):
    image_data = data["image"].split(",")[1]  # Remove o prefixo base64
    image_bytes = base64.b64decode(image_data)

    # Gerar um nome único para a imagem
    image_file_name = f"{uuid.uuid4()}.jpg"
    s3_client.put_object(Bucket=s3_bucket, Key=image_file_name, Body=image_bytes)

    try:
        session_id = data.get("user_id", "user123")  # Pegar o user_id
        lex_response = lex_client.recognize_text(
            botId=bot_id,
            botAliasId=bot_alias_id,
            localeId=locale_id,
            sessionId=session_id,
            text=image_file_name,  # Enviar o nome da imagem para o slot
        )

        # Verificar se o Lex respondeu
        if "messages" in lex_response and lex_response["messages"]:
            for msg in lex_response["messages"]:
                if "content" in msg:
                    socketio.emit("receive_message", {"message": msg["content"]})
        else:
            # Caso de fallback
            handle_fallback()

    except Exception as e:
        error_message = str(e)
        socketio.emit(
            "receive_message",
            {"message": f"Erro ao se comunicar com o bot: {error_message}"},
        )
        print(f"Erro: {error_message}")


if __name__ == "__main__":
    # Rodar o servidor Flask com suporte ao SocketIO
    socketio.run(app, host="0.0.0.0", port=5000)