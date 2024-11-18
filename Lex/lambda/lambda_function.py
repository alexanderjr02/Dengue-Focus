import boto3
from saudacoes import saudacoes_intent
from denunciaFoto import denunciaFoto_intent
from dicasTratamento import dicasTratamento_intent
from contato import contato_intent
from dicasPrevencao import dicasPrevencao_intent
from infereSintomas import infereSintomas_intent
from dicasDetect import dicasDetect_intent
from detectaSintoma import detectaSintoma_evento


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

    # Inferência sintomas
    elif current_intent == "InfereSintomasIntent":
        response = infereSintomas_intent(event)

    # Inferência sintomas
    elif current_intent == "DicasTratamentoDengue":
        response = dicasTratamento_intent(event)

    elif current_intent == "ContatoIntent":
        response = contato_intent(event)

    elif current_intent == "DicasPrevencaoIntent":
        response = dicasPrevencao_intent(event)

    elif current_intent == "DicasDectectIntent":
        response = dicasDetect_intent(event)

    elif current_intent == "SintomasDetectIntent":
        response = dicasDetect_intent(event)

    elif current_intent == "DetectaDorCabecaIntent":
        response = detectaSintoma_evento(event, "cefaleia")
    elif current_intent == "DetectaFebreIntent":
        response = detectaSintoma_evento(event, "febre")
    elif current_intent == "DetectaNauseaIntent":
        response = detectaSintoma_evento(event, "nausea")
    elif current_intent == "DetectaVomitoIntent":
        response = detectaSintoma_evento(event, "vomito")
    elif current_intent == "DetectaDorCorpoIntent":
        response = detectaSintoma_evento(event, "dor_corpo")
    elif current_intent == "DetectaDorCostasIntent":
        response = detectaSintoma_evento(event, "dor_costas")
    elif current_intent == "DetectaExantemaIntent":
        response = detectaSintoma_evento(event, "exantema")

    else:
        lex_message = "Desculpe, não entendi o que você disse."
        mensagem = f"{lex_message}"

        response = {
            "sessionState": {
                "dialogAction": {"type": "Close"},
                "intent": {"name": current_intent, "state": "Fulfilled"},
            },
            "messages": [
                {"contentType": "PlainText", "content": mensagem},
            ],
        }

    return response
