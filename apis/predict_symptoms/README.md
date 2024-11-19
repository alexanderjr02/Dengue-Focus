# API de previsão de Dengue baseado em sintomas

Este projeto implementa uma API de machine learning que prevê a probabilidade de dengue com base em sintomas usando XGBoost. A API é conteinerizada e implantada na AWS usando ECR e ECS.

## Estrutura do projeto

src/ analisys/ data/ predict/ api_symptoms.py # Main Flask API application Dockerfile # Docker configuration requirements.txt # Python dependencies


## Implementação da API

O arquivo `api_symptoms.py` é baseado:

- Configuração da API Flask com suporte a CORS
- Integração S3 para carregar o modelo XGBoost
- Ponto de extremidade de previsão que aceita dados de sintomas

## Docker Setup

1. Crie um `Dockerfile`:

```json
dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "api_symptoms.py"]
```

2.  Crie a imagem docker:

`docker build -t dengue-symptoms-api .`

# AWS Deployment

#### 1. Push to ECR

### Login no ECR

```json
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin {aws-account}.dkr.ecr.us-east-1.amazonaws.com
```

### Crie um repositório no ECR

```json
aws ecr create-repository --repository-name dengue-symptoms-api
```

### Tag image

```json
docker tag dengue-symptoms-api:latest {aws-account}.dkr.ecr.us-east-1.amazonaws.com/dengue-symptoms-api:latest
```

### Push image

```json
docker push {aws-account}.dkr.ecr.us-east-1.amazonaws.com/dengue-symptoms-api:latest
```

#### 2. ECS Setup

Configuração do ECS:

- Crie um cluster ECS.
- Crie uma Definição de Tarefa:
- Use uma imagem ECR
- Configure CPU/Memória
- Adicione variáveis ​​de ambiente

#### Crie um Serviço ECS:

- Escolha o cluster
- Configure a rede
- Configure um balanceador de carga, se necessário

Variáveis ​​de ambiente necessárias:

```json
- AWS_ACCESS_KEY_ID=xxx
- AWS_SECRET_ACCESS_KEY=xxx
- AWS_DEFAULT_REGION=us-east-1
```

# USO da API

Faça solicitações POST para /predict endpoint com dados de sintomas.

```json
{
  "febre": 0,
  "dor_corpo": 0,
  "dor_cabeca": 0,
  "erupcao": 0,
  "vomito": 1,
  "nausea": 0,
  "dor_costas": 0
}
```

rota para testar a inferência: http://18.212.236.202:5000/predict_symptoms

## Desenvolvimento local

1. Instalar dependências:

`pip install -r requirements.txt`

2. Executar localmente:

`python api_symptoms.py`

A API estará disponível em *http://localhost:5000*

#### Notas de segurança:

- Usar funções do IAM para tarefas do ECS
- Restringir acesso ao bucket do S3
- Configurar grupos de segurança
- Usar o AWS Secrets Manager para dados confidenciais

## Tecnologias Utilizadas

![Amazon S3](https://img.shields.io/badge/Amazon_S3-orange?logo=amazonaws&logoColor=white)
![Amazon CloudWatch](https://img.shields.io/badge/Amazon_CloudWatch-FF4F8B?logo=amazonaws&logoColor=white)
![Python 3.12](https://img.shields.io/badge/Python_3.12-3776AB?logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Amazon SageMaker](https://img.shields.io/badge/Amazon_SageMaker-232F3E?logo=amazonaws&logoColor=white)


- **Amazon S3**: Armazenamento do treinamento.
- **Amazon CloudWatch**: Monitoramento e logs da API.
- **Python 3.12**: Linguagem utilizada no desenvolvimento da aplicação.
- **Git**: Sistema de controle de versão para rastrear alterações e facilitar a colaboração.
- **Docker**: Sistema para criação da imagem
- **Sagemaker**: Treinamento do modelo
