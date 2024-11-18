# rekognition.py
import boto3

# Iniciando sessão Rekognition
cliente_rekognition = boto3.client("rekognition")

#dicionário de tradução/equivalência para as labels retornadas pelo rekognition
traducao_labels = {
    "pool": "piscina",
    "trash": "lixo",
    "drink": "água parada",
    "tire": "pneu",
    "water container": "recipiente com água",
    "puddle": "poças com água",
    "open container": "recipiente aberto",
    "bottle": "garrafa",
    "water bucket": "balde de água",
    "flower pot": "vaso de flores",
    "can": "lata",
    "waterpool": "piscina com água",
    "potted plant": "plantas em vaso",
    "jar": "jarro",
    "hot tub": "caixa d'água",
    "tub": "caixa d'água",
    "garbage": "lixo",
    "water": "água parada",
    "swimming pool": "piscina",
    "beverage": "líquidos",
    "cup": "xícaras",
    "glass": "copo",
    "bucket": "balde",
    "basin": "bacias",
    "fountain": "fontes com água",
    "pond": "lago",
    "yard": "quintal",
    "plant":"vaso de flores"
}


# Função para detectar locais suspeitos de proliferação de mosquitos utilizando labels
def detectar_locais_proliferacao(bucket, nome_imagem):
    print(f"Detectando locais na imagem: {nome_imagem} no bucket: {bucket}")
    
    resposta_labels = cliente_rekognition.detect_labels(
        Image={"S3Object": {"Bucket": bucket, "Name": nome_imagem}}, MaxLabels=10
    )
    
    locais_suspeitos = [
        "pool", "trash", "drink", "tire", "water container", "puddle",
        "open container", "bottle", "water bucket", "flower pot", "can", "waterpool",
        "pond", "water", "beer", "tub", "potted plant", "plant", "planter", "jar", "hot tub",
        "garbage", "swimming pool", "beverage", "cup", "glass", "bucket", "basin", "fountain",
        "pond", "fountain", "pond", "yard"
    ]

    locais_detectados = []
    local_suspeito = None

    for label in resposta_labels["Labels"]:
        if any(local in label["Name"].lower() for local in locais_suspeitos):
            
            nome_traduzido = traducao_labels.get(label["Name"].lower(), label["Name"])

            locais_detectados.append(
                {
                    "Nome": label["Name"],  # Nome original
                    "nome_traduzido": nome_traduzido,  # Nome traduzido
                    "Confiança": label["Confidence"],  # Nível de confiança
                }
            )

            if not local_suspeito:
                local_suspeito = {
                    "Nome": label["Name"],
                    "nome_traduzido": nome_traduzido,
                    "Confiança": label["Confidence"],
                }
    
    print(f"Respostas do Rekognition: {resposta_labels}")
    return locais_detectados, local_suspeito
