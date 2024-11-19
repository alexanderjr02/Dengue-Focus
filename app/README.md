# Documentação do Projeto - Diretório App

## Visão Geral
Este projeto é uma aplicação web interativa, desenvolvida em Python com o framework Flask, que utiliza tecnologias da AWS para oferecer funcionalidades como chat em tempo real, transcrição de áudio, conversão de texto em fala e análise de imagens. A comunicação em tempo real é realizada com Flask e SocketIO, e a aplicação integra os seguintes serviços da AWS:

- Amazon Lex para processamento de linguagem natural e interação via chatbot.
- Amazon Polly para conversão de texto em áudio (fala).
- Amazon Rekognition para análise de imagens enviadas pelos usuários.
- AWS S3 para armazenamento de áudios e imagens.

A aplicação permite que os usuários enviem texto, áudios e imagens, recebendo respostas em texto ou áudio, criando uma experiência dinâmica e interativa.<br>

## Tecnologias Utilizadas
![Flask](https://img.shields.io/badge/Flask-1.1.2-lightblue) ![SocketIO](https://img.shields.io/badge/SocketIO-4.0.1-yellow)  ![Amazon Lex](https://img.shields.io/badge/Amazon%20Lex-Ready-green)  ![Amazon Polly](https://img.shields.io/badge/Amazon%20Polly-TTS-orange)
![Amazon Rekognition](https://img.shields.io/badge/Amazon%20Rekognition-Image%20Analysis-purple) ![Amazon S3](https://img.shields.io/badge/Amazon%20S3-Storage-yellowgreen)
![Boto3](https://img.shields.io/badge/Boto3-1.24.5-blueviolet)
 ![Base64](https://img.shields.io/badge/Base64-Encoding%20%26%20Decoding-blue)

- Flask: Framework web para construção da aplicação.
- SocketIO: Biblioteca para comunicação em tempo real.
- Amazon Lex: Serviço da AWS para processamento de linguagem natural (chatbot).
- Amazon Polly: Serviço da AWS para conversão de texto em fala (TTS).
- Amazon Rekognition: Serviço da AWS para análise de imagens.
- Amazon S3: Armazenamento de arquivos como áudios e imagens.
- Boto3: Biblioteca Python para interagir com os serviços da AWS.
- Base64: Codificação e decodificação de áudios e imagens para transferência via Web.

## Estrutura de Diretórios
```
app/                                    # Diretório principal da aplicação
│
├── static/                             # Arquivos estáticos (CSS, JS, imagens)
│   ├── css/                            # Arquivos de estilo CSS
│   │    ├── chat.css                   # Estilos para a interface de chat
│   │    ├── header.css                 # Estilos para o cabeçalho
│   │    ├── home.css                   # Estilos para a página inicial
│   │    ├── resultado-esperado.css     # Estilos para a página de resultado esperado
│   │    └── style.css                  # Estilos gerais para a aplicação
│   ├── img/                            # Imagens usadas na aplicação
│   │    ├── logocompass.webp           # Logo do Compass
│   │    └── logoestacio.webp           # Logo da Estácio
│   └── js/                             # Scripts JavaScript
│        ├── input.js                   # Script para tratar inputs do usuário
│        ├── playAudio.js               # Script para reproduzir áudio
│        ├── script.js                  # Script principal de controle da aplicação
│        ├── sendAudio.js               # Envia áudio para o servidor
│        ├── sendImage.js               # Envia imagens para o servidor
│        └── sendMessage.js             # Envia mensagens do usuário para o servidor
│
├── templates/                          # Templates HTML renderizados pela aplicação
│   └── index.html                      # Página principal da aplicação
│
├── app.py                              # Código principal da aplicação Flask
├── config.py                           # Configurações da aplicação (por exemplo, chaves de acesso ao ambiente AWS)
├── requirements.txt                    # Lista de dependências da aplicação
├── stt.py                              # Código para conversão de fala em texto
├── tts.py                              # Código para conversão de texto em fala
└── README.md                           # Documentação da pasta app
```

## Como Executar Essa Aplicação

### Requisitos
Antes de executar a aplicação, verifique se os seguintes requisitos estão instalados:

- Python 3.x: A aplicação foi desenvolvida em Python, então você precisará do Python instalado em sua máquina.
- Pip: O gerenciador de pacotes do Python para instalar as dependências do projeto.
- Conta AWS: A aplicação utiliza serviços da AWS. Acesse a [documentação de configurações de ambiente da AWS](Lex\README.md) para configurar seu ambiente cloud.

### Passos para executar a aplicação
**1. Clone o repositório**: <br>
```
git clone -b grupo-2 https://github.com/Compass-pb-aws-2024-JUNHO/sprints-9-10-pb-aws-junho.git
```
**2. Crie um ambiente virtual (opcional, mas recomendado)**: Para isolar as dependências do projeto, você pode criar um ambiente virtual:
```
python3 -m venv venv
```
**3. Ative o ambiente virtual**:

**No Windows**:
```
venv\Scripts\activate
```
**No Linux/MacOS**:

```
source venv/bin/activate
```
**4. Instale as dependências**: Com o ambiente virtual ativo, instale as dependências necessárias para a aplicação:

```
pip install -r requirements.txt
```
**5. Configuração da AWS**: A aplicação interage com os serviços da AWS, por isso é necessário configurar suas credenciais:

**Instale o AWS CLI (se não estiver instalado) e configure suas credenciais**:
1. Instale o AWS CLI (se ainda não estiver instalado) e configure suas credenciais:
```
pip install awscli
aws configure
```

2. Durante a configuração, você precisará inserir suas credenciais da AWS (Access Key ID, Secret Access Key, região e formato de saída).

3. Verifique se as credenciais estão configuradas corretamente, testando o comando abaixo:

```
aws sts get-caller-identity
```
**6. Execute a aplicação**: Inicie a aplicação Flask:
```
python app.py
```
Isso iniciará o servidor Flask, e você verá uma saída semelhante a:

```
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```
A aplicação estará disponível em `http://localhost:5000`.

**7. Acesse a aplicação**: Abra o navegador e vá até `http://localhost:5000`. Você deverá ver a interface da aplicação.

## Considerações Finais
**Dependências da AWS**: A aplicação depende de serviços da AWS, como Amazon Lex, Polly, Rekognition e S3. Portanto, é importante garantir que as permissões e credenciais estejam configuradas corretamente.<br>

**Uso em Produção**: Se desejar usar a aplicação em um servidor remoto, substitua o endereço de localhost pelo IP ou domínio do servidor onde a aplicação está hospedada.
