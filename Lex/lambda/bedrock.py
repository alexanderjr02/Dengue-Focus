# bedrock.py
import boto3
import json

# Inicializando sessão com Bedrock
cliente_bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
translate = boto3.client('translate', region_name='us-east-1')


def traduzir_nome(nome, source_language='en', target_language='pt'):
    """Traduz o nome do item de inglês para português."""
    try:
        response = translate.translate_text(
            Text=nome,
            SourceLanguageCode=source_language,
            TargetLanguageCode=target_language
        )
        return response['TranslatedText']
    except Exception as e:
        print(f"Erro ao traduzir: {e}")
        return nome


def obter_dicas_dengue_bedrock(local_suspeito):
    local_suspeito = traduzir_nome(local_suspeito)


    print(f'local suspeito do bedrock: {local_suspeito}')
    entrada = (
        f"""Você é um especialista em saúde pública, focado na prevenção da dengue.
            Por favor, forneça dicas detalhadas sobre como eliminar e prevenir criadouros de mosquitos
            em locais como {local_suspeito}. Retorne 3 dicas no máximo, colocando a numeração a frente"""
    )
    
    modelo_id = "amazon.titan-text-express-v1"
    payload = {
        "inputText": entrada,
        "textGenerationConfig": {
            "maxTokenCount": 200,
            "temperature": 0.4,
            "topP": 0.9,
        },
    }
    
    print(f"Chamando Bedrock com a entrada: {entrada}")
    
    try:
        resposta = cliente_bedrock.invoke_model(
            modelId=modelo_id, body=json.dumps(payload), contentType="application/json"
        )
        resultado = json.loads(resposta["body"].read().decode("utf-8"))
        dica_dengue = resultado["results"][0]["outputText"].replace('\n', ' ')

        print(f"Dica retornada do Bedrock: {dica_dengue}")
        return dica_dengue

    except Exception as e:
        print(f"Erro ao acessar o Amazon Bedrock: {e}")
        return "Erro ao obter dicas de prevenção da dengue."

