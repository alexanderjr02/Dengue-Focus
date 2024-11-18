import json
import requests
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def parse_slot_value(slot_value):
    """
    Função para converter 'sim' para 1 e 'não' para 0.
    Se o valor for inválido, retorna 0.
    """
    if isinstance(slot_value, dict):
        slot_value = slot_value.get("interpretedValue", "não")

    if slot_value.lower() == "sim":
        return 1
    elif slot_value.lower() == "não":
        return 0
    else:
        return 0


def infereSintomas_intent(event):
    logging.info(
        "Recebendo evento para infereSintomas_intent: %s", json.dumps(event, indent=2)
    )

    # Recuperar sessionAttributes e slots
    session_attributes = event.get("sessionState", {}).get("sessionAttributes", {})
    slots = event["sessionState"]["intent"].get("slots", {})

    # Atualizar os slots com base nos sessionAttributes
    for key, value in session_attributes.items():
        if key in slots and not slots[key]:
            slots[key] = {"value": {"interpretedValue": value}}

    # Verificar se ainda há slots faltando
    required_slots = [
        "febre",
        "dor_corpo",
        "cefaleia",
        "exantema",
        "vomito",
        "nausea",
        "dor_costas",
    ]
    missing_slots = [
        slot
        for slot in required_slots
        if not slots.get(slot) or not slots[slot].get("value")
    ]

    if missing_slots:
        # Solicitar ao usuário preencher o próximo slot
        slot_to_elicit = missing_slots[0]
        logging.info(f"Solicitando ao usuário preencher o slot: {slot_to_elicit}")
        return {
            "sessionState": {
                "dialogAction": {"type": "ElicitSlot", "slotToElicit": slot_to_elicit},
                "intent": {
                    "name": "InfereSintomasIntent",
                    "slots": slots,
                    "state": "InProgress",
                },
                "sessionAttributes": session_attributes,  # Preserva os atributos da sessão
            },
            "responseCard": {
                "version": 1,
                "contentType": "application/vnd.amazonaws.card.generic",
                "genericAttachments": [
                    {
                        "title": f"Você tem {slot_to_elicit.replace('_', ' ')}?",
                        "subTitle": "Por favor, selecione uma opção.",
                        "buttons": [
                            {"text": "Sim", "value": "sim"},
                            {"text": "Não", "value": "não"},
                        ],
                    }
                ],
            },
        }

    # Converter os valores dos slots para enviar à API
    data = {
        "febre": parse_slot_value(slots.get("febre", {}).get("value")),
        "dor_corpo": parse_slot_value(slots.get("dor_corpo", {}).get("value")),
        "dor_cabeca": parse_slot_value(slots.get("cefaleia", {}).get("value")),
        "erupcao": parse_slot_value(slots.get("exantema", {}).get("value")),
        "vomito": parse_slot_value(slots.get("vomito", {}).get("value")),
        "nausea": parse_slot_value(slots.get("nausea", {}).get("value")),
        "dor_costas": parse_slot_value(slots.get("dor_costas", {}).get("value")),
    }

    logging.info("Dados preparados para envio à API: %s", json.dumps(data, indent=2))

    try:
        # Enviar os dados para a API
        response = requests.post(
            "http://18.212.236.202:5000/predict_symptoms",
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )

        logging.info(
            "Resposta da API: Status Code %s, Corpo: %s",
            response.status_code,
            response.text,
        )

        if response.status_code == 404:
            raise Exception("Endpoint da API não encontrado.")
        elif response.status_code != 200:
            raise Exception(f"API request failed with status {response.status_code}")

        prediction = response.json().get("prediction", 0)

        if prediction == 1:
            mensagem = "Os sintomas indicam que você pode estar com dengue. Recomendamos que você procure um médico para confirmação."
        else:
            mensagem = "Os sintomas não indicam dengue, mas se você continuar se sentindo mal, procure um médico para avaliação."

    except Exception as e:
        logging.error(f"Erro na requisição à API: {e}")
        mensagem = "Desculpe, houve um erro ao processar sua solicitação. Tente novamente mais tarde."

    # Responder ao usuário com o resultado
    response = {
        "sessionState": {
            "dialogAction": {"type": "Close"},
            "intent": {"name": "InfereSintomasIntent", "state": "Fulfilled"},
            "sessionAttributes": session_attributes,  # Mantém os sessionAttributes para continuidade
        },
        "messages": [
            {"contentType": "PlainText", "content": mensagem},
            {
                "contentType": "PlainText",
                "content": "Obrigado por usar o DengueBot. Se precisar de algo mais, é só falar.",
            },
        ],
    }

    logging.info("Resposta para o Lex: %s", json.dumps(response, indent=2))
    return response
