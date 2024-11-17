import boto3
from rekognition import detectar_locais_proliferacao
from bedrock import obter_dicas_dengue_bedrock


# Inicializa o cliente S3
s3_client = boto3.client("s3")


def verifica_imagem_s3(bucket_name, nome_imagem):
    """Verifica se a imagem existe no bucket S3."""

    print(f"Verificando imagem no bucket '{bucket_name}' com nome '{nome_imagem}'")

    try:
        s3_client.head_object(Bucket=bucket_name, Key=nome_imagem)
        print(f"Imagem {nome_imagem} encontrada no S3.")
        return True
    except Exception as e:
        print(f"Erro ao buscar a imagem no S3: {str(e)}")
        return False


def denunciaFoto_intent(event):
    # Verifica se a intenção e os slots estão presentes
    if (
        "sessionState" not in event
        or "intent" not in event["sessionState"]
        or "slots" not in event["sessionState"]["intent"]
    ):
        print("Evento inválido recebido.")
        return {
            "sessionState": {
                "dialogAction": {"type": "Close"},
                "intent": {
                    "name": event["sessionState"]["intent"]["name"],
                    "state": "Failed",
                },
            },
            "messages": [
                {"contentType": "PlainText", "content": "Evento inválido."},
            ],
        }

    # Verifica se o slot nomeImagem existe e se tem valor
    slots = event["sessionState"]["intent"]["slots"]
    nome_imagem = slots.get(
        "nomeImagem"
    )  # Não usar .get() em um dicionário potencialmente vazio

    if not nome_imagem or not nome_imagem.get("value"):
        print("Slot 'nomeImagem' não encontrado ou vazio.")
        return {
            "sessionState": {
                "dialogAction": {"type": "ElicitSlot", "slotToElicit": "nomeImagem"},
                "intent": {
                    "name": event["sessionState"]["intent"]["name"],
                    "state": "InProgress",
                },
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": "Por favor, forneça o nome da imagem.",
                },
            ],
        }

    # Recupera o valor original do slot nomeImagem
    nome_imagem_value = nome_imagem.get("value").get("originalValue")

    # Verifica se o nome da imagem foi passado corretamente
    if not nome_imagem_value:
        print("Nome da imagem não encontrado.")
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
                    "content": "Nome da imagem não foi fornecido.",
                },
            ],
        }

    # Verifica se a imagem existe no bucket S3
    bucket_name = "denguefoto"
    if not verifica_imagem_s3(bucket_name, nome_imagem_value):
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
                    "content": f"Imagem {nome_imagem_value} não encontrada no S3.",
                },
            ],
        }

    # Usa o Rekognition para detectar locais suspeitos na imagem
    locais_detectados, local_suspeito = detectar_locais_proliferacao(
        bucket_name, nome_imagem_value
    )

    # Verifica se locais suspeitos foram encontrados
    mensagem_risco = (
        "Locais suspeitos de proliferação de dengue foram identificados."
        if locais_detectados
        else "Nenhum local suspeito de proliferação de dengue foi identificado na imagem."
    )
    # print(locais_detectados, local_suspeito)

    # # Usa o Bedrock para obter dicas de prevenção
    try:
        if local_suspeito:
            print(f"Entrou no if do bedrock: {local_suspeito['Nome']}")
            dicas_prevencao = obter_dicas_dengue_bedrock(local_suspeito["Nome"])
            print(f"Dicas de prevenção: {dicas_prevencao}")
        else:
            dicas_prevencao = (
                "Lembre-se de não deixar água parada e tampar recipientes."
            )
    except Exception as e:
        print(f"Erro ao obter dicas de prevenção com o Bedrock: {str(e)}")
        dicas_prevencao = "Não foi possível obter dicas de prevenção no momento."

    # Retorna a resposta para o usuário
    return {
        "sessionState": {
            "dialogAction": {"type": "Close"},
            "intent": {
                "name": event["sessionState"]["intent"]["name"],
                "state": "Fulfilled",
            },
        },
        "messages": [
            {"contentType": "PlainText", "content": mensagem_risco},
            {"contentType": "PlainText", "content": dicas_prevencao},
        ],
    }
