import boto3

def contato_intent(event):
    
    # Mensagens sobre os cuidados com a dengue
    message = "❗ Não se preocupe! Caso não seja seguro remover o foco do mosquito ou precise de apoio, aqui estão algumas formas de obter ajuda:"
    message1 = "📞 Disque Saúde - Telefone 199: Canal direto para denúncias sobre focos de dengue."
    message2 = "📞 Ouvidoria Geral do GDF - Telefone 162: Para denúncias e informações gerais sobre saúde pública."
    message3 = "📲 Brasília Ambiental: Registre focos de dengue e solicite inspeções online: https://www.ibram.df.gov.br"
    message4 = "🔔 Sua segurança é muito importante! Se precisar, entre em contato para tratar o foco de maneira segura."
    message5 = "🤝 Juntos, podemos combater a dengue. Estamos aqui para ajudar no que for preciso!"

    # Estrutura de resposta para o Lex já com os aúdios pra cada mensagem
    response = {
        "sessionState": {
            "dialogAction": {"type": "Close"},
            "intent": {"name": event["sessionState"]["intent"]["name"], "state": "Fulfilled"},
        },
        "messages": [
            {"contentType": "PlainText", "content": message},
            {"contentType": "PlainText", "content": message1},
            {"contentType": "PlainText", "content": message2},
            {"contentType": "PlainText", "content": message3},
            {"contentType": "PlainText", "content": message4},
            {"contentType": "PlainText", "content": message5},
        ],
    }

    return response