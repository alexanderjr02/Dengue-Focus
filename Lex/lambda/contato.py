import boto3

def contato_intent(event):
    
    # Mensagens sobre os cuidados com a dengue
    message = "Caso você não tenha acesso ao foco de dengue ou ache que não é capaz de lidar com essa situação, entre em contato: "
    message1 = "Você pode ligar para os números: 199 ou 193"
    message2 = "Para fazer reclamações: https://www.participa.df.gov.br/pages/registro-manifestacao/relato"


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
        ],
    }

    return response
