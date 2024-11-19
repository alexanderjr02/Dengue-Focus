from flask import Flask, render_template, session
from flask_socketio import SocketIO, join_room, emit
import boto3
import base64
import os
import uuid
from stt import transcribe_audio
import json
from tts import get_audio_url_from_tts
from dotenv import load_dotenv
from config import Config

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
app.config.from_object(Config)
socketio = SocketIO(app, cors_allowed_origins="*")
s3_bucket_name = "projeto-final-grupo-2"

# AWS Configuration
aws_config = {
    "region_name": app.config["AWS_DEFAULT_REGION"],
    "aws_access_key_id": app.config["AWS_ACCESS_KEY_ID"],
    "aws_secret_access_key": app.config["AWS_SECRET_ACCESS_KEY"],
}

if app.config.get("AWS_SESSION_TOKEN"):
    aws_config["aws_session_token"] = app.config["AWS_SESSION_TOKEN"]

# Initialize AWS clients
try:
    lex_client = boto3.client("lexv2-runtime", **aws_config)
    s3_client = boto3.client("s3", **aws_config)
    transcribe_client = boto3.client("transcribe", **aws_config)
except Exception as e:
    print(f"Error initializing AWS clients: {str(e)}")

# Lex V2 configuration
bot_id = "KF1FJWESHS"
bot_alias_id = "TSTALIASID"
locale_id = "pt_BR"


@app.before_request
def ensure_session_id():
    if "sessionId" not in session:
        session["sessionId"] = str(uuid.uuid4())


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("connect")
def handle_connect(auth=None):
    if "sessionId" not in session:
        session["sessionId"] = str(uuid.uuid4())
    current_session = session["sessionId"]
    join_room(current_session)
    return True


@socketio.on("send_message")
def handle_message(data):
    user_message = data["message"]
    current_session = session.get("sessionId")

    try:
        response = lex_client.recognize_text(
            botId=bot_id,
            botAliasId=bot_alias_id,
            localeId=locale_id,
            sessionId=current_session,
            text=user_message,
        )

        if "messages" in response and response["messages"]:
            for msg in response["messages"]:
                if (
                    msg.get("contentType") == "PlainText"
                    and "content" in msg
                    and msg["content"]
                ):
                    audio_url = get_audio_url_from_tts(msg["content"])
                    socketio.emit(
                        "receive_message",
                        {"message": msg["content"], "audioUrl": audio_url},
                        room=current_session,
                    )
                elif msg.get("contentType") == "ImageResponseCard":
                    card = msg["imageResponseCard"]
                    buttons = card.get("buttons", [])
                    socketio.emit(
                        "receive_card",
                        {"title": card["title"], "buttons": buttons},
                        room=current_session,
                    )
                else:
                    # Handle empty content field
                    socketio.emit(
                        "receive_message",
                        {
                            "message": "Desculpe, houve um problema ao processar sua mensagem. Tente novamente."
                        },
                        room=current_session,
                    )
        else:
            handle_fallback(current_session)

    except Exception as e:
        error_message = str(e)
        socketio.emit(
            "receive_message",
            {"message": f"Erro ao se comunicar com o bot: {error_message}"},
            room=current_session,
        )
        print(f"Erro: {error_message}")


def handle_fallback(current_session):
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
    socketio.emit(
        "receive_message", {"message": fallback_message}, room=current_session
    )
    socketio.emit("receive_card", card_response, room=current_session)


@socketio.on("send_audio")
def handle_audio(data):
    current_session = session.get("sessionId")
    try:
        audio_data = data["audio"].split(",")[1]
        audio_bytes = base64.b64decode(audio_data)

        audio_file_name = f"audio/{current_session}_user_audio.mp3"
        s3_client.put_object(
            Bucket=s3_bucket_name, Key=audio_file_name, Body=audio_bytes
        )

        audio_content_base64 = base64.b64encode(audio_bytes).decode("utf-8")
        transcription_result = transcribe_audio(audio_content_base64)
        transcript_text = json.loads(transcription_result["body"])["transcript"]

        response = lex_client.recognize_text(
            botId=bot_id,
            botAliasId=bot_alias_id,
            localeId=locale_id,
            sessionId=current_session,
            text=transcript_text,
        )

        if "messages" in response and response["messages"]:
            for msg in response["messages"]:
                if "content" in msg:
                    socketio.emit(
                        "receive_message",
                        {"message": msg["content"]},
                        room=current_session,
                    )
                if msg.get("contentType") == "ImageResponseCard":
                    card = msg["imageResponseCard"]
                    buttons = card.get("buttons", [])
                    socketio.emit(
                        "receive_card",
                        {"title": card["title"], "buttons": buttons},
                        room=current_session,
                    )
        else:
            handle_fallback(current_session)

    except Exception as e:
        error_message = str(e)
        socketio.emit(
            "receive_message",
            {"message": f"Erro ao processar a transcrição: {error_message}"},
            room=current_session,
        )


@socketio.on("send_image")
def handle_image(data):
    current_session = session.get("sessionId")
    try:
        image_data = data["image"].split(",")[1]
        image_bytes = base64.b64decode(image_data)
        image_file_name = f"images/{current_session}_{uuid.uuid4()}.jpg"

        s3_client.put_object(
            Bucket=s3_bucket_name, Key=image_file_name, Body=image_bytes
        )

        lex_response = lex_client.recognize_text(
            botId=bot_id,
            botAliasId=bot_alias_id,
            localeId=locale_id,
            sessionId=current_session,
            text=image_file_name,
        )

        if "messages" in lex_response and lex_response["messages"]:
            for msg in lex_response["messages"]:
                if "content" in msg:
                    socketio.emit(
                        "receive_message",
                        {"message": msg["content"]},
                        room=current_session,
                    )
                if msg.get("contentType") == "ImageResponseCard":
                    card = msg["imageResponseCard"]
                    buttons = card.get("buttons", [])
                    socketio.emit(
                        "receive_card",
                        {"title": card["title"], "buttons": buttons},
                        room=current_session,
                    )
        else:
            handle_fallback(current_session)

    except Exception as e:
        error_message = str(e)
        socketio.emit(
            "receive_message",
            {"message": f"Erro ao processar imagem: {error_message}"},
            room=current_session,
        )
        print(f"Erro: {error_message}")


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)