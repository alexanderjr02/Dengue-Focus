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
    # if not verifica_imagem_s3(bucket_name, nome_imagem):
    #     return {
    #         "sessionState": {
    #             "dialogAction": {"type": "Close"},
    #             "intent": {"name": current_intent, "state": "Failed"},
    #         },
    #         "messages": [
    #             {
    #                 "contentType": "PlainText",
    #                 "content": f"A imagem '{nome_imagem}' não foi encontrada no sistema.",
    #             },
    #         ],
    #     }
    if not verifica_imagem_s3(bucket_name, nome_imagem):
        slots["nomeImagem"] = (
            None  # Limpa o slot nomeImagem para permitir uma nova tentativa
        )
        return {
            "sessionState": {
                "dialogAction": {"type": "ElicitSlot", "slotToElicit": "nomeImagem"},
                "intent": {"name": current_intent, "slots": slots},
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": f"A imagem não foi encontrada no sistema. Por favor, envie outra imagem.",
                },
            ],
        }

    # Detecta locais suspeitos usando Rekognition
    if not label_slot or not label_slot.get("value", {}).get("originalValue"):
        locais_detectados, local_suspeito = detectar_locais_proliferacao(
            bucket_name, nome_imagem
        )
        if local_suspeito:
            label_detectado = local_suspeito["Nome"]
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
            slots["label"] = None  # apaga a label antiga (que estaria "errada")
            slots["confirmacao"] = None  # evita loop eterno de uma mente sem lembranças

            # user preenche manualmente o valor do slot label
            return {
                "sessionState": {
                    "dialogAction": {
                        "type": "ElicitSlot",  # Solicita ao usuário para preencher o slot
                        "slotToElicit": "label",  # Especifica qual slot será preenchido
                    },
                    "intent": {
                        "name": current_intent,
                        "slots": slots,  # Passa os slots para o estado da sessão-> label vazio
                    },
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": "Por favor, descreva o que você identificou na imagem.",  # Mensagem para o usuário
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
            dicas_prevencao = obter_dicas_dengue_bedrock(novo_label)
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
                {"contentType": "PlainText", "content": dicas_prevencao},
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
