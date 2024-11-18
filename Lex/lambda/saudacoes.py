
def saudacoes_intent(event):
    current_intent = event["sessionState"]["intent"]["name"]

    print(f"Intent: {current_intent}, Slots: {event['sessionState']['intent']['slots']}")

    lex_message = f"Olá! Bem-vindo ao Chatbot de Monitoramento de Dengue! Selecione o que deseja fazer"

    action_type = "Close"  
    # Estrutura do card de resposta
    card_response = {
        "contentType": "ImageResponseCard",
        "imageResponseCard": {
            "title": "Como posso te ajudar?",
            "buttons": [
                {"text": "Análise de Foco por Imagem", "value": "Análise de foco por imagem"},
                {"text": "Verificar Sintomas", "value": "Sintomas"},
                {"text": "Dicas de Prevenção", "value": "Prevenção"},
                {"text": "Dicas de Tratamento ", "value": "Tratamento"},
                {"text": "Informação para Contato ", "value": "Informação para contato"},

                
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
            card_response,  
        ],
    }

    return response