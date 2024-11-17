# from utils import get_audio_url_from_tts


def saudacoes_intent(event):
    current_intent = event["sessionState"]["intent"]["name"]

    # lex_message = "Selecione uma opção para atendimento: Caso queira agendar uma consulta, clique em Agendar, caso queira verificar uma consulta, clique em verificar e caso queira cancelar uma consulta, clique em cancelar"
    lex_message = f"Olá! Bem-vindo ao Chatbot de Monitoramento de Dengue! Selecione o que deseja fazer"

    # url_audio = get_audio_url_from_tts(lex_message)
    # mensagem2 = (
    #     f"Ouça o áudio aqui: {url_audio}" if url_audio else "Áudio não disponível"
    # )

    action_type = "Close"

    # Estrutura do card de resposta
    card_response = {
        "contentType": "ImageResponseCard",
        "imageResponseCard": {
            "title": "Como posso te ajudar?",
            "buttons": [
                {"text": "Reportar foco de dengue", "value": "Reportar foco de dengue"},
                {"text": "Reportar sintomas", "value": "Sintomas"},
                {"text": "Tirar dúvidas", "value": "Dúvidas"},
                {
                    "text": "Informar-se sobre sintomas da dengue",
                    "value": "Info Sintomas",
                },
            ],
        },
    }

    response = {
        "sessionState": {
            "dialogAction": {
                "type": action_type,
                "slotToElicit": None,
            },
            "intent": {
                "name": current_intent,
                "slots": {},
                "state": "Fulfilled",
            },
        },
        "messages": [
            {"contentType": "PlainText", "content": lex_message},
            # {"contentType": "PlainText", "content": mensagem2},
            card_response,
        ],
    }

    return response
