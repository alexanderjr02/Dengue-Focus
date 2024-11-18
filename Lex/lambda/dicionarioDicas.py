import random

# Dicionário de dicas para prevenção da dengue - para labels
dicas_dengue = {
    "lixo": [
        "Feche bem os sacos de lixo e mantenha as lixeiras tampadas para não acumular água.",
        "Coloque o lixo em sacos plásticos bem fechados e cubra a lixeira.",
        "Evite deixar lixo ao ar livre, pois pode acumular água e se tornar foco de dengue.",
        "Mantenha as lixeiras tampadas e retire o lixo com frequência para evitar criadouros.",
    ],
    "pneu": [
        "Evite acumular pneus velhos no quintal, pois podem acumular água da chuva.",
        "Guarde pneus em locais cobertos ou fure-os para evitar que acumulem água.",
        "Descarte pneus velhos de maneira adequada para evitar o acúmulo de água e a proliferação do mosquito.",
        "Mantenha pneus velhos longe de áreas com água parada.",
    ],
    "água parada": [
        "Elimine qualquer recipiente que possa acumular água, como latas, potes e garrafas.",
        "Verifique se há água acumulada em calhas, e limpe-as regularmente.",
        "Tampe caixas d'água e outros reservatórios para evitar a entrada do mosquito.",
        "Evite deixar pratos de plantas com água; limpe-os e troque a areia regularmente.",
    ],
    "piscina": [
        "Trate a água da piscina com cloro regularmente, mesmo que ela não esteja em uso.",
        "Cubra a piscina quando não estiver em uso para evitar o acúmulo de água parada.",
        "Mantenha a água da piscina sempre limpa e tratada para evitar criadouros.",
        "Inspecione frequentemente a área ao redor da piscina em busca de criadouros.",
    ],
    "recipiente com água": [
        "Tampe ou elimine recipientes que possam acumular água da chuva.",
        "Não deixe garrafas ou potes jogados em locais expostos à chuva.",
        "Lave os recipientes regularmente com água e sabão para evitar larvas.",
    ],
    "poças com água": [
        "Preencha buracos ou depressões no solo para evitar o acúmulo de água.",
        "Evite deixar vasos ou pratos com água acumulada expostos à chuva.",
        "Inspecione regularmente o quintal e elimine poças d'água.",
    ],
    "vaso de flores": [
        "Troque a água dos vasos de flores diariamente e lave-os com frequência.",
        "Evite usar vasos que acumulam água no fundo.",
        "Coloque areia grossa nos pratinhos das plantas para evitar o acúmulo de água.",
    ],
    "plantas em vaso": [
        "Regue apenas o necessário para evitar acúmulo de água nos vasos.",
        "Inspecione vasos semanalmente para evitar criadouros escondidos.",
        "Coloque areia nos pratos de vasos para impedir a formação de larvas de mosquito.",
    ],
    "jarro": [
        "Lave e seque jarros regularmente para evitar o acúmulo de larvas.",
        "Evite deixar jarros com água por longos períodos.",
        "Armazene jarros vazios de cabeça para baixo.",
    ],
    "caixa d'água": [
        "Mantenha a caixa d'água sempre bem tampada para evitar a entrada de mosquitos.",
        "Inspecione regularmente a vedação da tampa da caixa d'água.",
        "Faça a limpeza periódica da caixa d'água para evitar acúmulo de sujeira.",
    ],
    "balde de água": [
        "Cubra os baldes com tampas adequadas ou elimine a água quando não for utilizada.",
        "Evite deixar baldes de água expostos à chuva.",
        "Guarde baldes em locais cobertos para evitar o acúmulo de água.",
    ],
    "xícaras": [
        "Lave as xícaras regularmente para evitar acúmulo de água.",
        "Evite deixar xícaras expostas à chuva, especialmente em áreas externas.",
        "Armazene as xícaras em locais protegidos e secos.",
    ],
    "copo": [
        "Descarte copos descartáveis de forma adequada para evitar acúmulo de água.",
        "Lave copos reutilizáveis imediatamente após o uso.",
        "Armazene copos de cabeça para baixo em locais cobertos.",
    ],
    "bacias": [
        "Evite deixar bacias com água acumulada expostas ao ambiente.",
        "Cubra as bacias ou descarte a água imediatamente após o uso.",
        "Guarde bacias vazias em locais secos e protegidos.",
    ],
    "lata": [
        "Descarte latas de maneira adequada para evitar o acúmulo de água.",
        "Amasse ou perfure latas antes de jogá-las fora para impedir que acumulem água.",
        "Evite deixar latas espalhadas em áreas externas expostas à chuva.",
    ],
    "lago": [
        "Adicione peixes em lagos ornamentais para ajudar a controlar a proliferação de mosquitos.",
        "Mantenha a água do lago em movimento com bombas ou fontes.",
        "Limpe os lagos regularmente para remover larvas e sujeiras.",
    ],
    "quintal": [
        "Inspecione o quintal semanalmente e elimine criadouros como pneus, garrafas e latas.",
        "Evite acumular entulhos no quintal, pois podem se tornar focos de dengue.",
        "Mantenha o quintal limpo e livre de objetos que possam acumular água.",
    ],
    "fontes com água": [
        "Limpe as fontes regularmente para evitar o acúmulo de sujeira e larvas.",
        "Adicione peixes ou utilize produtos químicos para evitar a proliferação de mosquitos.",
        "Certifique-se de que a água da fonte esteja sempre em movimento.",
    ],
}


def obter_dica_aleatoria(
    label_traduzido,
):  # Retorna uma dica aleatória para a prevenção da dengue baseada no rótulo traduzido.
    label = label_traduzido.lower()  # Normaliza para letras minúsculas
    if label in dicas_dengue:
        return random.choice(dicas_dengue[label])
    else:
        return "Não há dicas disponíveis para este item. Verifique o rótulo fornecido."
