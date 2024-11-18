import boto3


def dicasTratamento_intent(event):
    # Mensagem principal com orientações básicas de cuidados com a dengue
    # message = (
    #     "Aqui estão algumas orientações básicas para o cuidado de uma pessoa com suspeita de dengue:\n\n"
    #     "1. Hidratação: É muito importante beber bastante líquido, como água, sucos naturais e água de coco. A hidratação ajuda a evitar complicações.\n\n"
    #     "2. Repouso: Descanso é essencial para ajudar o corpo a combater a infecção.\n\n"
    #     "3. Evitar Medicamentos sem Prescrição: Não tome medicamentos sem orientação médica, especialmente aqueles que contêm ácido acetilsalicílico (aspirina), pois podem aumentar o risco de sangramento.\n\n"
    #     "4. Monitorar Sinais de Alerta: Fique atento a sintomas mais graves, como dores abdominais intensas, vômitos persistentes, tonturas, sangramentos ou manchas roxas na pele. Se algum desses sintomas aparecer, procure atendimento médico imediatamente.\n\n"
    #     "Se precisar de mais informações ou se tiver sintomas graves, é fundamental buscar ajuda médica."
    # )
    message = "Aqui estão algumas orientações básicas para o cuidado de uma pessoa com suspeita de dengue:\n\n"
    message1 = "1. Hidratação: É muito importante beber bastante líquido, como água, sucos naturais e água de coco. A hidratação ajuda a evitar complicações.\n\n"
    message2 = "2. Repouso: Descanso é essencial para ajudar o corpo a combater a infecção.\n\n"
    message3 = "3. Evitar Medicamentos sem Prescrição: Não tome medicamentos sem orientação médica, especialmente aqueles que contêm ácido acetilsalicílico (aspirina), pois podem aumentar o risco de sangramento.\n\n"
    message4 = "4. Monitorar Sinais de Alerta: Fique atento a sintomas mais graves, como dores abdominais intensas, vômitos persistentes, tonturas, sangramentos ou manchas roxas na pele. Se algum desses sintomas aparecer, procure atendimento médico imediatamente.\n\n"

    message5 = "Se precisar de mais informações ou se tiver sintomas graves, é fundamental buscar ajuda médica."

    # Estrutura de resposta para o Lex
    response = {
        "sessionState": {
            "dialogAction": {"type": "Close"},
            "intent": {
                "name": event["sessionState"]["intent"]["name"],
                "state": "Fulfilled",
            },
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

    # return {
    #     "sessionState": {
    #         "dialogAction": {"type": "Close"},
    #         "intent": {"name": event["sessionState"]["intent"]["name"], "state": "Fulfilled"},
    #     },
    #     "messages": [
    #         {"contentType": "PlainText", "content": mensagem_risco},
    #     ],
    # }
