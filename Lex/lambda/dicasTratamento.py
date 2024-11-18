import boto3
import random


def dicasTratamento_intent(event):
    # Listas de mensagens sobre os cuidados com a dengue
    mensagens = [
        "Aqui estão algumas orientações básicas para o cuidado de uma pessoa com suspeita de dengue:\n\n",
        "Veja a seguir algumas orientações importantes para ajudar quem pode estar com dengue:\n\n",
        "Estas são recomendações iniciais para o cuidado de uma pessoa com sintomas de dengue:\n\n",
    ]

    dicas = [
        [
            "1. Hidratação: É muito importante beber bastante líquido, como água, sucos naturais e água de coco. A hidratação ajuda a evitar complicações.\n\n",
            "1. Hidratação: Beber muitos líquidos, como água, sucos naturais e água de coco, é fundamental para evitar complicações.\n\n",
            "1. Hidratação: Manter-se bem hidratado, com água e sucos, é essencial para reduzir riscos de agravamento.\n\n",
            "1. Hidratação: Consumir bastante líquido, incluindo água e sucos naturais, ajuda a prevenir problemas mais graves.\n\n",
        ],
        [
            "2. Repouso: Descanso é essencial para ajudar o corpo a combater a infecção.\n\n",
            "2. Repouso: Descansar é essencial para que o organismo consiga combater o vírus.\n\n",
            "2. Repouso: Dar ao corpo o descanso necessário ajuda a fortalecer a recuperação.\n\n",
            "2. Repouso: Manter-se em repouso é importante para que o corpo tenha mais força contra a infecção.\n\n",
        ],
        [
            "3. Evitar Medicamentos sem Prescrição: Não tome medicamentos sem orientação médica, especialmente aqueles que contêm ácido acetilsalicílico (aspirina), pois podem aumentar o risco de sangramento.\n\n",
            "3. Evite Medicamentos sem Orientação: Não use remédios sem consultar um médico, especialmente os que contêm aspirina, pois podem provocar sangramentos.\n\n",
            "3. Evite Automedicação: Não tome medicamentos por conta própria, principalmente aspirina, para evitar riscos de sangramento.\n\n",
            "3. Medicamentos com Cuidado: Evite tomar qualquer medicamento sem prescrição, especialmente aspirina, devido ao risco de sangramentos.\n\n",
        ],
        [
            "4. Monitorar Sinais de Alerta: Fique atento a sintomas mais graves, como dores abdominais intensas, vômitos persistentes, tonturas, sangramentos ou manchas roxas na pele. Se algum desses sintomas aparecer, procure atendimento médico imediatamente.\n\n",
            "4. Atenção aos Sinais de Alerta: Fique atento a sintomas graves, como fortes dores abdominais, vômitos, tontura, sangramentos ou manchas roxas. Se surgirem, procure atendimento médico.\n\n",
            "4. Monitore os Sinais de Perigo: Observe se surgem dores abdominais intensas, vômitos, tontura ou sangramentos. Esses sintomas exigem avaliação médica urgente.\n\n",
            "4. Sinais de Alerta: Esteja atento a sintomas como dores abdominais intensas, vômitos persistentes e manchas roxas. Na presença desses sinais, procure ajuda médica imediatamente.\n\n",
        ],
        [
            "Se precisar de mais informações ou se tiver sintomas graves, é fundamental buscar ajuda médica.",
            "Se precisar de mais orientações ou tiver sintomas graves, é importante procurar um médico.",
            "Para mais informações ou em caso de sintomas graves, consulte um profissional de saúde.",
            "Se você tiver dúvidas ou apresentar sintomas intensos, busque ajuda médica o quanto antes.",
        ],
    ]

    # Sorteando aleatoriamente uma mensagem de introdução e uma dica de cada categoria
    message = random.choice(mensagens)
    message1 = random.choice(dicas[0])
    message2 = random.choice(dicas[1])
    message3 = random.choice(dicas[2])
    message4 = random.choice(dicas[3])
    message5 = random.choice(dicas[4])

    # Estrutura de resposta para o Lex já com os áudios para cada mensagem
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
