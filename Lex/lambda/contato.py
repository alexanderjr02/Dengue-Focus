import boto3

def contato_intent(event):
    
    # Mensagens sobre os cuidados com a dengue
    message = "Caso você não tenha acesso ao foco de dengue ou ache que não é capaz de lidar com essa situação, entre em contato: "
    message1 = "Telefone: xxxxxxxxx"
    message2 = "Email: xxxx@gmail.com"


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
