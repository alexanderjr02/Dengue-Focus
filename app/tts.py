import boto3
import hashlib
from datetime import datetime

# Configurações AWS
polly_client = boto3.client("polly", region_name="us-east-1")
s3_client = boto3.client("s3", region_name="us-east-1")
dynamodb = boto3.resource("dynamodb", region_name="us-east-1")

# Bucket S3 e tabela DynamoDB
s3_bucket_name = "projeto-final-grupo-2"
dynamo_table_name = "projeto-final-grupo2"
table = dynamodb.Table(dynamo_table_name)


def get_audio_url_from_tts(phrase):
    """
    Converte o texto fornecido em fala usando AWS Polly e retorna a URL do áudio no S3.
    """
    try:
        # Verificação de entrada
        if not phrase:
            raise ValueError("Nenhuma frase fornecida para o TTS")

        # Cria um identificador único para a frase
        unique_id = hashlib.md5(phrase.encode("utf-8")).hexdigest()[:10]
        audio_file_name = f"{unique_id}.mp3"

        # Verifica se o áudio já existe no DynamoDB
        response = table.get_item(Key={"unique_id": unique_id})
        if "Item" in response:
            return response["Item"]["url_to_audio"]

        # Verifica se o áudio já existe no S3
        try:
            s3_client.head_object(Bucket=s3_bucket_name, Key=audio_file_name)
            audio_url = f"https://{s3_bucket_name}.s3.amazonaws.com/{audio_file_name}"
        except s3_client.exceptions.ClientError:
            # Se o áudio não existir no S3, sintetiza com Polly
            response_polly = polly_client.synthesize_speech(
                Text=phrase, OutputFormat="mp3", VoiceId="Ricardo"
                
            )
            audio_stream = response_polly["AudioStream"].read()

            # Salva o áudio no S3
            s3_client.put_object(
                Bucket=s3_bucket_name,
                Key=audio_file_name,
                Body=audio_stream,
                ContentType="audio/mpeg",
            )
            audio_url = f"https://{s3_bucket_name}.s3.amazonaws.com/{audio_file_name}"

            # Salva a informação no DynamoDB
            created_audio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            table.put_item(
                Item={
                    "unique_id": unique_id,
                    "received_phrase": phrase,
                    "url_to_audio": audio_url,
                    "created_audio": created_audio,
                }
            )

        return audio_url

    except Exception as e:
        print(f"Erro no TTS: {str(e)}")
        raise e
