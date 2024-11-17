import boto3
from saudacoes import saudacoes_intent
from denunciaFoto import denunciaFoto_intent


def lambda_handler(event, context):
    # recuperando a entrada do Lex
    print(f"Evento recebido: {event}")

    current_intent = event["sessionState"]["intent"]["name"]
    slots = event["sessionState"]["intent"]["slots"]
    session_attributes = event["sessionState"].get("sessionAttributes", {})

    # SaudacaoIntent com geração de áudio
    if current_intent == "Saudacoes":
        response = saudacoes_intent(event)

    # Denúncia com foto
    elif current_intent == "DenunciaFotoIntent":
        response = denunciaFoto_intent(event)

    else:
        lex_message = "Desculpe, não entendi o que você disse."
        mensagem = f"{lex_message}"

        # url_audio = get_audio_url_from_tts(lex_message)
        # mensagem2 = (
        #     f"Ouça o áudio aqui: {url_audio}" if url_audio else "Áudio não disponível"
        # )
        response = {
            "sessionState": {
                "dialogAction": {"type": "Close"},
                "intent": {"name": current_intent, "state": "Fulfilled"},
            },
            "messages": [
                {"contentType": "PlainText", "content": mensagem},
                # {"contentType": "PlainText", "content": mensagem2},
            ],
        }

    return response