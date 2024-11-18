import boto3
import random
from rekognition import detectar_locais_proliferacao
from bedrock import obter_dicas_dengue_bedrock

# from cohere_utils import obter_dicas_dengue_cohere
from dicionarioDicas import obter_dica_aleatoria
# from gpt import obter_dicas_dengue_gpt


# Inicializa o cliente S3
s3_client = boto3.client("s3")

# Variável de controle de tentativas no escopo global
tentativas_falhas = 0

# Mensagens variadas para falhas
mensagens_falha = [
    "A imagem não foi encontrada no sistema. Por favor, tente novamente.",
    "Parece que houve um problema com a imagem. Por favor, envie outra.",
    "Não conseguimos localizar a imagem no sistema. Tente enviar novamente.",
    "A imagem enviada não foi encontrada. Por favor, envie uma nova imagem.",
    "Houve um erro ao processar a imagem. Por favor, tente outra.",
]


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
    global tentativas_falhas  # Controla as falhas globalmente dentro da intent

    # Obtém a intenção e slots do evento
    current_intent = event["sessionState"]["intent"]["name"]
    slots = event["sessionState"]["intent"]["slots"]
    nome_imagem_slot = slots.get("nomeImagem")
    label_slot = slots.get("label")
    confirmacao_slot = slots.get("confirmacao")

    # Verifica se o slot "nomeImagem" está preenchido
    if not nome_imagem_slot or not nome_imagem_slot.get("value", {}).get(
        "originalValue"
    ):
        return {
            "sessionState": {
                "dialogAction": {"type": "ElicitSlot", "slotToElicit": "nomeImagem"},
                "intent": {"name": current_intent, "slots": slots},
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": "Por favor, envie a imagem que deseja verificar.",
                },
            ],
        }

    nome_imagem = nome_imagem_slot["value"]["originalValue"]
    bucket_name = "denguefoto"

    # Verifica se a imagem existe no S3
    if not verifica_imagem_s3(bucket_name, nome_imagem):
        # Incrementa o contador de falhas
        tentativas_falhas += 1

        # Verifica se atingiu o limite de 3 falhas
        if tentativas_falhas >= 3:
            card_response = {
                "contentType": "ImageResponseCard",
                "imageResponseCard": {
                    "title": "Como posso te ajudar?",
                    "buttons": [
                        {
                            "text": "Reportar foco de dengue",
                            "value": "Reportar foco de dengue",
                        },
                        {"text": "Verificar sintomas", "value": "Sintomas"},
                        {"text": "Dicas de Prevenção", "value": "Prevenção"},
                        {"text": "Dicas de tratamento", "value": "Tratamento"},
                        {
                            "text": "Informação para contato",
                            "value": "Informação para contato",
                        },
                    ],
                },
            }

            # Reinicia o contador de falhas
            tentativas_falhas = 0
            return {
                "sessionState": {
                    "dialogAction": {"type": "Close"},
                    "intent": {"name": current_intent, "state": "Failed"},
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": "Parece que você está tendo problemas com o nosso chat. Vamos te ajudar.",
                    },
                    card_response,
                ],
            }

        # Caso não tenha atingido o limite, solicita outra imagem com mensagem aleatória
        slots["nomeImagem"] = (
            None  # Limpa o slot nomeImagem para permitir uma nova tentativa
        )
        mensagem_falha = random.choice(
            mensagens_falha
        )  # Seleciona uma mensagem aleatória
        return {
            "sessionState": {
                "dialogAction": {"type": "ElicitSlot", "slotToElicit": "nomeImagem"},
                "intent": {"name": current_intent, "slots": slots},
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": mensagem_falha,
                },
            ],
        }

    # Detecta locais suspeitos usando Rekognition
    if not label_slot or not label_slot.get("value", {}).get("originalValue"):
        locais_detectados, local_suspeito = detectar_locais_proliferacao(
            bucket_name, nome_imagem
        )
        if local_suspeito:
            label_detectado = local_suspeito["nome_traduzido"]
            print(f"Oi estou conferindo meu bug {label_detectado}")

            # Atualiza o slot label com o valor detectado
            slots["label"] = {
                "value": {
                    "originalValue": label_detectado,
                    "interpretedValue": label_detectado,
                }
            }

            return {
                "sessionState": {
                    "dialogAction": {
                        "type": "ElicitSlot",
                        "slotToElicit": "confirmacao",
                    },
                    "intent": {"name": current_intent, "slots": slots},
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": f"Detectamos um possível '{label_detectado}' na imagem. Você confirma essa identificação?",
                    },
                ],
            }
        else:
            return {
                "sessionState": {
                    "dialogAction": {"type": "Close"},
                    "intent": {"name": current_intent, "state": "Failed"},
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": "Nenhum local suspeito foi identificado na imagem.",
                    },
                ],
            }

    # Verifica a confirmação do usuário
    if confirmacao_slot:
        resposta_confirmacao = confirmacao_slot["value"]["interpretedValue"].lower()
        print(f"A minha resposta é: {resposta_confirmacao}")

        if resposta_confirmacao == "não":
            slots["label"] = None  # Apaga a label antiga
            slots["confirmacao"] = None  # Evita loops desnecessários

            # Solicita ao usuário que preencha o slot label
            return {
                "sessionState": {
                    "dialogAction": {"type": "ElicitSlot", "slotToElicit": "label"},
                    "intent": {"name": current_intent, "slots": slots},
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": "Por favor, descreva o que você identificou na imagem.",
                    },
                ],
            }
        elif resposta_confirmacao == "sim":
            # Confirma o label e segue o fluxo
            print(
                f"Usuário confirmou a identificação: {label_slot['value']['originalValue']}"
            )

    # Verifica se o slot "label" foi preenchido manualmente ou confirmado
    if label_slot and label_slot.get("value", {}).get("originalValue"):
        novo_label = label_slot["value"]["originalValue"]
        slots["label"] = {
            "value": {
                "originalValue": novo_label,
                "interpretedValue": novo_label,
            }
        }
        print(f"Novo label definido pelo usuário: {novo_label}")

        try:
            dicas_prevencao = obter_dicas_dengue_bedrock(novo_label)  # fora do ar hehe
            # dicas_prevencao = obter_dica_aleatoria(novo_label)
            # dicas_prevencao = obter_dicas_dengue_gpt(novo_label)
            dicas = dicas_prevencao.split("2. ")
            dica1 = "1 - " + dicas[0].replace("1. ", "").strip()
            dica2 = "2 - " + dicas[1].split("3. ")[0].strip() if len(dicas) > 1 else ""
            dica3 = (
                "3 - " + dicas[1].split("3. ")[1].strip()
                if len(dicas[1].split("3. ")) > 1
                else ""
            )
        except Exception as e:
            print(f"Erro ao obter dicas de prevenção: {str(e)}")
            dicas_prevencao = "Não foi possível obter dicas de prevenção no momento. BedRock está fora do ar"

        # Mensagem final
        mensagem_risco = (
            "Locais suspeitos de proliferação de dengue foram identificados."
        )
        return {
            "sessionState": {
                "dialogAction": {"type": "Close"},
                "intent": {"name": current_intent, "state": "Fulfilled"},
            },
            "messages": [
                {"contentType": "PlainText", "content": mensagem_risco},
                {"contentType": "PlainText", "content": dica1},
                {"contentType": "PlainText", "content": dica2},
                {"contentType": "PlainText", "content": dica3},
                {
                    "contentType": "PlainText",
                    "content": "Obrigado por usar o DengueBot. Se precisar de algo mais, é só falar.",
                },
            ],
        }

    # Caso nenhum fluxo seja ativado
    return {
        "sessionState": {
            "dialogAction": {"type": "ElicitSlot", "slotToElicit": "label"},
            "intent": {"name": current_intent, "slots": slots},
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": "Ainda precisamos que você confirme ou preencha o rótulo da imagem.",
            },
        ],
    }
