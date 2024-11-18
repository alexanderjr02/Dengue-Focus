import json
import boto3
import base64
import requests
from datetime import datetime
import time

# Configurações AWS para Transcribe e S3
transcribe_client = boto3.client("transcribe")
s3_client = boto3.client("s3")

# Nome do bucket S3 para armazenar o áudio
s3_bucket_name = "projeto-final-grupo2"


def transcribe_audio(audio_content_base64):
    """Transcreve o áudio enviado em base64 usando Amazon Transcribe e retorna o texto transcrito."""
    try:
        # Decodifica o áudio de base64 para bytes
        audio_data = base64.b64decode(audio_content_base64)

        # Gera um nome único para o arquivo de áudio
        audio_key = f'audio-{datetime.now().strftime("%Y%m%d%H%M%S")}.mp3'

        # Faz upload do áudio para o S3
        s3_client.put_object(
            Bucket=s3_bucket_name,
            Key=audio_key,
            Body=audio_data,
            ContentType="audio/mpeg",
        )

        # URL do áudio no S3
        audio_url = f"s3://{s3_bucket_name}/{audio_key}"

        # Nome único para o trabalho de transcrição
        job_name = f'transcription-{datetime.now().strftime("%Y%m%d%H%M%S")}'

        # Inicia a transcrição com o Amazon Transcribe
        transcribe_client.start_transcription_job(
            TranscriptionJobName=job_name,
            Media={"MediaFileUri": audio_url},
            MediaFormat="mp3",
            LanguageCode="pt-BR",
        )

        # Espera a transcrição ser concluída
        while True:
            status = transcribe_client.get_transcription_job(
                TranscriptionJobName=job_name
            )
            job_status = status["TranscriptionJob"]["TranscriptionJobStatus"]
            if job_status == "COMPLETED":
                transcript_url = status["TranscriptionJob"]["Transcript"][
                    "TranscriptFileUri"
                ]
                transcript_text = get_transcript_text(transcript_url)
                return {
                    "statusCode": 200,
                    "body": json.dumps(
                        {
                            "message": "Transcription completed",
                            "transcript": transcript_text,
                        }
                    ),
                }
            elif job_status == "FAILED":
                return {
                    "statusCode": 500,
                    "body": json.dumps({"message": "Transcription job failed"}),
                }
            else:
                print("Transcription in progress...")
                time.sleep(
                    5
                )  # Ta verificando se a transcrição já concluiu a cada 5 segundos

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(
                {"message": "Error processing the request", "error": str(e)}
            ),
        }


def get_transcript_text(transcript_url):
    """Obtém o texto transcrito a partir do URL JSON do Amazon Transcribe."""
    response = requests.get(transcript_url)
    transcript_data = response.json()
    return transcript_data["results"]["transcripts"][0]["transcript"]
