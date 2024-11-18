def dicasDetect_intent(event):
    # Mensagem para o usuário
    message = "Você gostaria de dicas sobre prevenção ou tratamento da dengue?"

    # Card de resposta com botões
    card_response = {
        "contentType": "ImageResponseCard",
        "imageResponseCard": {
            "title": "Selecione uma opção",
            "buttons": [
                {"text": "Dicas de Prevenção", "value": "Dicas de Prevenção"},
                {"text": "Dicas de Tratamento", "value": "Dicas de Tratamento"},
            ],
        },
    }

    # Construção da resposta
    response = {
        "sessionState": {
            "dialogAction": {
                "type": "ElicitIntent"
            },  # Espera uma nova intent baseada na escolha
            "intent": {"name": "DicasDectectIntent", "state": "InProgress"},
        },
        "messages": [
            {"contentType": "PlainText", "content": message},
            card_response,
        ],
    }
    return response
