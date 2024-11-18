# rekognition.py
import boto3

# Iniciando sessão Rekognition
cliente_rekognition = boto3.client("rekognition")

# Função para detectar locais suspeitos de proliferação de mosquitos utilizando labels
def detectar_locais_proliferacao(bucket, nome_imagem):
    print(f"Detectando locais na imagem: {nome_imagem} no bucket: {bucket}")
    
    resposta_labels = cliente_rekognition.detect_labels(
        Image={"S3Object": {"Bucket": bucket, "Name": nome_imagem}}, MaxLabels=10
    )
    
    locais_suspeitos = [
        "pool", "trash", "drink", "tire", "water container", "puddle",
        "open container", "bottle", "water bucket", "flower pot", "can",
        "pond", "water", "beer", "tub", "potted plant", "plant", "planter"
    ]

    locais_detectados = []
    local_suspeito = None

    for label in resposta_labels["Labels"]:
        if any(local in label["Name"].lower() for local in locais_suspeitos):
            locais_detectados.append(
                {"Nome": label["Name"], "Confiança": label["Confidence"]}
            )

            if not local_suspeito:
                local_suspeito = {"Nome": label["Name"], "Confiança": label["Confidence"]}
    
    print(f"Respostas do Rekognition: {resposta_labels}")
    return locais_detectados, local_suspeito
