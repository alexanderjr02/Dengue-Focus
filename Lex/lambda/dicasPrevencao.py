import boto3
import random

# Dicas de prevenção contra a dengue (separadas por dentro e fora de casa)
dicas_dengue_dentro = [
    "Elimine recipientes que acumulem água, como latas e garrafas.",
    "Mantenha caixas d'água, tambores e poços cobertos.",
    "Limpe calhas e telhados regularmente para evitar acúmulo de água.",
    "Coloque areia até a borda dos pratos de vasos de plantas.",
    "Mantenha piscinas tratadas com cloro e limpas regularmente.",
    "Remova água acumulada em pneus e guarde-os em locais cobertos.",
    "Troque a água dos vasos de plantas aquáticas semanalmente.",
    "Limpe e cubra ralos externos que podem acumular água.",
    "Use repelentes para evitar picadas de mosquito.",
    "Utilize telas em portas e janelas para impedir a entrada de mosquitos.",
    "Limpe semanalmente os bebedouros de animais domésticos.",
    "Evite plantas que acumulam água nas folhas, como bromélias.",
    "Tampe todos os recipientes que possam armazenar água.",
    "Armazene garrafas de cabeça para baixo para evitar acúmulo de água.",
    "Limpe bandejas de ar-condicionado regularmente.",
    "Evite deixar brinquedos ou utensílios que acumulem água no quintal.",
    "Use roupas que cubram a maior parte do corpo em áreas com muitos mosquitos.",
    "Inspecione sua residência semanalmente em busca de focos de água parada.",
    "Evite armazenar água em baldes ou recipientes descobertos.",
]

dicas_dengue_fora = [
    "Verifique e elimine água de lajes e áreas externas.",
    "Evite deixar sacos plásticos expostos ao ar livre.",
    "Descarte corretamente o lixo e mantenha-o em recipientes fechados.",
    "Incentive vizinhos a manterem suas casas livres de criadouros.",
    "Evite jogar lixo em terrenos baldios ou áreas abertas.",
    "Solicite a retirada de entulhos ou objetos abandonados em terrenos.",
    "Não acumule folhas ou entulhos que possam reter água.",
    "Realize mutirões comunitários de limpeza com frequência.",
    "Coloque telas protetoras em caixas de esgoto e fossas sépticas.",
    "Esteja atento a campanhas locais de combate à dengue e participe delas.",
]


def dicasPrevencao_intent(event):
    # Seleciona 2 dicas de dentro de casa e 2 dicas de fora de casa
    dicas_dentro = random.sample(dicas_dengue_dentro, 2)
    dicas_fora = random.sample(dicas_dengue_fora, 2)

    # Junta as dicas selecionadas
    dicas_selecionadas = dicas_dentro + dicas_fora

    # Embaralha a lista de dicas selecionadas para garantir a aleatoriedade
    random.shuffle(dicas_selecionadas)

    # Constrói mensagens de dicas
    message_intro = "Aqui estão algumas dicas de prevenção contra a dengue para que voce possa se proteger tanto dentro, quanto fora de casa:\n\n"
    message1 = f"1. {dicas_selecionadas[0]}\n\n"
    message2 = f"2. {dicas_selecionadas[1]}\n\n"
    message3 = f"3. {dicas_selecionadas[2]}\n\n"
    message4 = f"4. {dicas_selecionadas[3]}\n\n"
    message_final = "Se você tiver mais dúvidas ou precisar de mais informações, não hesite em entrar em contato novamente. Estamos aqui para ajudar!"

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
            {"contentType": "PlainText", "content": message_intro},
            {"contentType": "PlainText", "content": message1},
            {"contentType": "PlainText", "content": message2},
            {"contentType": "PlainText", "content": message3},
            {"contentType": "PlainText", "content": message4},
            {"contentType": "PlainText", "content": message_final},
        ],
    }

    return response
