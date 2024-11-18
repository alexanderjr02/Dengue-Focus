def detectaSintoma_evento(event, sintoma):
    """
    Armazena o sintoma detectado nos sessionAttributes e redireciona para a intent principal.
    """
    try:
        # Recuperar sessionAttributes existentes ou inicializar um novo dicionário
        session_attributes = event["sessionState"].get("sessionAttributes", {})

        # Atualizar o sessionAttribute com o sintoma detectado
        session_attributes[sintoma] = "sim"

        # Redirecionar para a intent principal
        response = {
            "sessionState": {
                "dialogAction": {"type": "Delegate"},  # Delegar o controle
                "intent": {
                    "name": "InfereSintomasIntent",  # Nome da intent principal
                    "slots": {},  # Slots serão preenchidos usando sessionAttributes
                    "state": "InProgress",
                },
                "sessionAttributes": session_attributes,  # Enviar os sessionAttributes atualizados
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": "Vejo que está com um dos sintomas da dengue, vamos fazer mais perguntas para avaliar sua situação.",
                },
                {
                    "contentType": "PlainText",
                    "content": f"Entendido, você mencionou {sintoma.replace('_', ' ')}. Vamos continuar com mais perguntas.",
                },
            ],
        }

        return response

    except Exception as e:
        # Tratamento de erro caso algo dê errado
        print(f"Erro ao processar o sintoma {sintoma}: {e}")
        return {
            "sessionState": {
                "dialogAction": {"type": "Close"},
                "intent": {
                    "name": event["sessionState"]["intent"]["name"],
                    "state": "Failed",
                },
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": "Ocorreu um erro ao processar sua solicitação. Tente novamente mais tarde.",
                },
            ],
        }
