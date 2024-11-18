import json
import boto3
import hashlib
import base64
import os
from datetime import datetime

# Configurando boto3 para AWS Polly, S3 e DynamoDB
polly_client = boto3.client('polly')
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('denguettsdynamo') # Nome da tabela de vcs tbm
s3_bucket_name = 'denguetts'  # Pode colocar o nome da bucket de vcs

def get_audio_url_from_tts(phrase):
    """Converte texto em fala usando AWS Polly e retorna a URL do áudio armazenado no S3."""
    try:
        if not phrase:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'No phrase provided', 'error_code': 'MISSING_PHRASE'})
            }

        # Cria um identificador único para a frase
        unique_id = hashlib.md5(phrase.encode('utf-8')).hexdigest()[:10]
        audio_file_name = f"{unique_id}.mp3"

        # Verifica se o áudio já existe no DynamoDB
        response = table.get_item(Key={'unique_id': unique_id})
        if 'Item' in response:
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Audio already exists', 'url_to_audio': response['Item']['url_to_audio']})
            }

        # Verifica se o áudio já existe no S3 como cache adicional
        try:
            s3_client.head_object(Bucket=s3_bucket_name, Key=audio_file_name)
            # Gera a URL do objeto existente no S3
            audio_url = f"https://{s3_bucket_name}.s3.amazonaws.com/{audio_file_name}"
        except s3_client.exceptions.ClientError:
            # Se o áudio não existir no S3, usa o Polly para sintetizar
            response_polly = polly_client.synthesize_speech(
                Text=phrase, OutputFormat='mp3', VoiceId='Ricardo'
            )
            audio_stream = response_polly['AudioStream'].read()

            # Salva o áudio no S3
            s3_client.put_object(
                Bucket=s3_bucket_name,
                Key=audio_file_name,
                Body=audio_stream,
                ContentType='audio/mpeg'
            )
            audio_url = f"https://{s3_bucket_name}.s3.amazonaws.com/{audio_file_name}"

        # Codifica o áudio em base64, se desejado
        audio_base64 = base64.b64encode(audio_stream).decode('utf-8')

        # Salva as informações no DynamoDB
        created_audio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        table.put_item(
            Item={
                'unique_id': unique_id,
                'received_phrase': phrase,
                'url_to_audio': audio_url,
                'created_audio': created_audio
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Audio generated successfully',
                'url_to_audio': audio_url,
                #'audio_base64': audio_base64 Não quero visualizar isso agora.
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error processing the request', 'error': str(e)})
        }



