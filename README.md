![banner_denguebot](https://github.com/user-attachments/assets/6683707b-dafc-43d4-b498-14879a4cfea3)

# <p align="center">Dengue Focus: Chatbot de Apoio no Combate e Prevenção de Focos de Dengue

<p align="center">
<img src="https://badgen.net/badge/STATUS/CONCLUÍDO/green?icon=github" alt="Status Badge"/>
  <img src="https://badgen.net/badge/Version/1.0.0/blue?icon=github" alt="Version Badge"/>
</p>

## ⚙️Versão

Atualmente está disponível a **Versão 1.0.0** do presente projeto, disponibilizada em Novembro/2024.

## 📝 Descrição
Este projeto é um chatbot desenvolvido para auxiliar na identificação e combate aos focos de dengue. Ele também oferece alternativas de tratamento, realiza um pré-diagnóstico da doença e orienta os usuários a procurarem ajuda das autoridades sanitárias e médicas.

## 💪 Nossa Motivação
A dengue é uma doença de alta incidência e grande impacto social, especialmente em áreas tropicais. No entanto, a falta de informações claras sobre como identificar focos do mosquito transmissor e os primeiros sinais da doença frequentemente atrasa a resposta e o tratamento adequados. Este projeto foi criado para facilitar o acesso a essas informações, melhorar a resposta pública e acelerar o diagnóstico e tratamento.

## ⚠️ Problema A Ser Resolvido
A falta de conhecimento da população sobre a prevenção de focos do mosquito Aedes aegypti e os sintomas da dengue compromete a eficácia das ações de combate à doença. Além disso, a ausência de um sistema centralizado de conscientização e orientação dificulta a resposta rápida das autoridades de saúde pública.

## 💡 Nossa Solução
O Dengue Focus oferece uma solução interativa que permite aos usuários identificar focos de dengue, receber orientação sobre prevenção e tratamento, e realizar um pré-diagnóstico. Além disso, ele contribui para a conscientização coletiva e apoia as autoridades de saúde pública na otimização das ações no combate à dengue.

## 👥 Nosso Cliente
Nossa aplicação foi desenvolvida em parceria com a Secretaria de Saúde, mais especificamente com a equipe da área ambiental. O objetivo é melhorar as estratégias de combate aos focos de dengue e otimizar a resposta à epidemia, contribuindo para ações mais rápidas e eficazes.

## 📋 Funcionalidades

### **As principais funções do Dengue Focus são**:

- Identificação de focos de dengue: Análise de imagens para detectar possíveis criadouros do mosquito transmissor.
- Orientação e conscientização: Informações sobre sintomas, prevenção e combate à dengue.
- Pré-diagnóstico: Diagnóstico preliminar com base nos sintomas relatados, utilizando um modelo de machine learning.
- Dicas personalizadas: Sugestões para prevenção e respostas à doença.
- Instruções de Contato Com Autoridades: Oferece formas de contato com autoridades locais para o controle e prevenção de casos de dengue.

## 👀 Preview da Aplicação
![Gif da aplicação DengueBot](https://github.com/user-attachments/assets/df937324-45af-41ae-bac1-c2db0dd5605c)


## ⚙️ Tecnologias Utilizadas

### 🛠️ Linguagens e Frameworks<br>
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![HTML](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

- **Python**: Linguagem de programação utilizada no desenvolvimento do chatbot.
- **Flask**: Framework leve e flexível para a criação de aplicações web.
- **HTM**L: Usado para estruturar o conteúdo da interface do chatbot.
- **CSS**: Utilizado para estilizar o layout e criar uma interface atraente.
- **JavaScript**: Adicionado para interatividade e dinamismo à interface web.

### ☁️ Serviços da AWS <br>
![AWS Lambda](https://img.shields.io/badge/AWS%20Lambda-F7B93E?style=for-the-badge&logo=amazonaws&logoColor=black) ![AWS Lex](https://img.shields.io/badge/AWS%20Lex-1A73E8?style=for-the-badge&logo=amazonaws&logoColor=white) ![AWS Rekognition](https://img.shields.io/badge/AWS%20Rekognition-00C7B7?style=for-the-badge&logo=amazonaws&logoColor=white) ![AWS Bedrock](https://img.shields.io/badge/AWS%20Bedrock-663399?style=for-the-badge&logo=amazonaws&logoColor=white) ![AWS Polly](https://img.shields.io/badge/AWS%20Polly-5E60CE?style=for-the-badge&logo=amazonaws&logoColor=white) ![AWS Transcribe](https://img.shields.io/badge/AWS%20Transcribe-FF6F61?style=for-the-badge&logo=amazonaws&logoColor=white) ![AWS Translate](https://img.shields.io/badge/AWS%20Translate-2EB67D?style=for-the-badge&logo=amazonaws&logoColor=white) ![AWS S3](https://img.shields.io/badge/AWS%20S3-569A31?style=for-the-badge&logo=amazonaws&logoColor=white) ![DynamoDB](https://img.shields.io/badge/DynamoDB-4053D6?style=for-the-badge&logo=amazondynamodb&logoColor=white) ![Amazon SageMaker](https://img.shields.io/badge/Amazon%20SageMaker-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)

- **AWS Lambda**: Executa o código do chatbot sem necessidade de gerenciamento de servidores.
- **AWS Lex**: Serviço utilizado para criar o chatbot que interage com o usuário, processando entrada de texto ou aúdio, reconhecendo intenções e retornando respostas em texto ou áudio.
- **AWS Rekognition**: Analisa imagens para identificar focos de dengue.
- **AWS Bedrock**: Gera dicas personalizadas com IA avançada sobre combate à dengue.
- **AWS Polly**: Converte texto em áudio para respostas do chatbot.
- **AWS Transcribe**: Converte áudio dos usuários em texto.
- **AWS Translate**: Serviço de tradução automática que converte texto entre diferentes idiomas, permitindo a conversão dos labels identificados em inglês para o português.
- **AWS S3**: Utilizado para armazenar os arquivos de áudio gerados pela AWS Polly. O S3 atua como um repositório onde os áudios são salvos e disponibilizados para acesso via URL. Além de também armazenar as imagens enviadas pelos usuários do chatbot para que sejam analisadas pelo AWS Rekognition.
- **DynamoDB**: Um banco de dados NoSQL usado para armazenar as referências dos áudios gerados, como o hash único da frase e o link do áudio. Isso permite verificar se um áudio já foi criado anteriormente.
- **AWS SageMaker**: Foi usado nesse projeto para treinar um modelo de machine learning que realiza diagnósticos iniciais da dengue com base nos sintomas relatados pelos usuários. 

## 🛠 Como Abrir e Executar Esse Projeto

  Para executar essa aplicação, acesse a [documentação de configurações de ambiente da AWS](./Lex/README.md) para configurar o seu ambiente cloud, e acesse a [documentação de configuração do ambiente local](./app/README.md) para rodar a aplicação localmente. <br>

**É importante a realização dos passos conforme a documentação para que sua aplicação funcione corretamente**.

## 🏗️ Arquitetura da Aplicação

![Arquitetura_da Aplicacao](https://github.com/user-attachments/assets/a55899d8-510c-4ecc-87f0-611aecf00d00)

## 📂 Estrutura do Projeto
### Estrutura de Diretórios: 

```
Sprints-9-10-PB-AWS-JUNHO/
├── Lex/
│    ├── Bot_Final/                      
│    │      ├── DengueBot_FINAL.zip       # Versão final do bot para upload no AWS Lex.
│    │      ├── DengueBot_v7.zip          # Iteração final do bot no AWS Lex.
│    │      └── Lambda_Final.zip          # Funções Lambda necessárias para o bot.
│    ├── Layers/
│    │      └── Lib-Requests.zip          # Biblioteca Requests empacotada como layer para Lambda.
│    ├── Lex_Antigos/
│    │      └── ...                       # Arquivos de versões anteriores do Lex.
│    ├── lambda/
│    │      ├── bedrock.py                # Interage com o Bedrock para gerar respostas.
│    │      ├── contato.py                # Gera respostas relacionadas a contato.
│    │      ├── denunciaFoto.py           # Analisa possiveis focos de dengue imagens enviadas através do chatbot.
│    │      ├── detectaSintomas.py        # Identifica sintomas relatados pelos usuários.
│    │      ├── dicasDetect.py            # Identifica o sintoma indicado pelo usuário e o captura em um slot para a intent infereSintomas
│    │      ├── dicasPrevencao.py         # Retorna dicas de prevenção relacionadas à dengue.
│    │      ├── dicasTratamento.py        # Sugere tratamentos gerais para a dengue.
│    │      ├── dicionarioDicas.py        # Contém um dicionário com dicas pré-definidas.
│    │      ├── infereSintomas.py         # Faz inferências com base nos sintomas relatados.
│    │      ├── lambda_function.py        # Função Lambda principal para execução no AWS.
│    │      ├── rekognition.py            # Processa imagens usando Amazon Rekognition.
│    │      └── saudacoes.py              # Responde com saudações iniciais.
│    └── README.md                        # Documentação sobre os recursos do AWS Lex.
├── analysis/                           
│    ├── data/
│    │      └── ...                       # Dados usados para análises do projeto.
│    ├── sagemaker/ 
│    │      ├── prever_casos_train.py     # Script para treinar modelo preditivo no SageMaker.
│    │      └── sagemaker_prever_sintomas.ipynb  # Notebook para prever sintomas no SageMaker.
│    │
│    └── modelo_prever_sintomas.ipynb     # Notebook para análise e modelagem de sintomas.
├── apis/
│    ├── templates/
│    │      └── index.html                # Template HTML para endpoints da API.
│    ├── .dockerignore                    # Ignora arquivos desnecessários ao construir a imagem Docker.
│    ├── README.md                        # Documentação da API.
│    ├── api_symptoms.py                  # API para processar sintomas e enviar respostas.
│    ├── dockerfile                       # Configuração do container Docker da API.
│    └── requirements.txt                 # Dependências da API.
├── app/
│    ├── static/
│    │     ├── css/
│    │     │    ├── chat.css              # Estilo para a interface de chat.
│    │     │    ├── header.css            # Estilo para o cabeçalho da página.
│    │     │    ├── home.css              # Estilo para a página inicial.
│    │     │    ├── resultado-esperado.css  # Estilo para resultados esperados.
│    │     │    └── style.css             # Estilos gerais da aplicação.
│    │     ├── image/
│    │     │    ├── logocompass.webp      # Logo da Compass utilizado no projeto.
│    │     │    └── logoestacio.webp      # Logo da Estácio utilizado no projeto.
│    │     └── js/
│    │          ├── input.js              # Processa entradas do usuário.
│    │          ├── playAudio.js          # Controla reprodução de áudios.
│    │          ├── script.js             # Script principal para lógica da página.
│    │          ├── sendAudio.js          # Envia áudios via API.
│    │          ├── sendImage.js          # Envia imagens via API.
│    │          └── sendMessage.js        # Envia mensagens de texto via API.
│    │
│    ├── templates/
│    │     └── index.html                 # Template da página inicial.
│    ├── README.md                        # Documentação do app web.
│    ├── app.py                           # Script principal da aplicação web.
│    ├── config.py                        # Configurações gerais da aplicação.
│    ├── requirements.txt                 # Dependências da aplicação web.
│    ├── stt.py                           # Processa conversão de fala para texto.
│    └── tts.py                           # Converte texto em fala.
├── assets/
│    ├── images/
│    │     ├── Arquitetura_Aplicacao.jpg  # Diagrama da arquitetura final da aplicação.
│    │     ├── banner_denguebot.jpg       # Banner promocional do DengueBot.
│    │     └── esboco_arquitetura_inicial.png  # Rascunho da arquitetura inicial.
│    └── videos/
│          └── DengueGif.gif              # GIF ilustrativo sobre o DengueBot.
├── docs/
│    ├── proposta-cliente/
│    │     └── proposta_cliente.pdf       # Proposta do projeto enviada ao cliente.
│    └── proposta_projeto_final.pdf       # Proposta protótipo documentada do projeto.
├── .dockerignore                         # Ignora arquivos específicos ao criar imagens Docker.
├── .gitignore                            # Lista de arquivos e pastas ignorados pelo Git.
├── README.md                             # Documentação principal do repositório.
└── dockerfile                            # Configuração principal para a imagem Docker.
```


## 😵‍💫 Dificuldades Encontradas

- **Complexidade na Engenharia de Prompt**: A manipulação de labels, parâmetros e prompts no Amazon Bedrock exigiu um conhecimento mais avançado em engenharia de prompt. Isso foi essencial para gerar conteúdo adequado e útil, e demandou inúmeras iterações até encontrar o formato ideal. Testamos diferentes formas de estruturação dos prompts e ajustamos os parâmetros até que as respostas geradas fossem mais amigáveis e fáceis de ler. <br>

- **Treinamento do Modelo**: Pré-processamento dos dados e quais parâmetros utilizar. A base de dados original para o treinamento do modelo era extensa, e requeriu um pré-processamento robusto para que apenas os dados relevantes fossem mantidos para o treinamento do modelo utilizado.

- **Dificuldade em criar a imagem Docker da aplicação**: Ao tentar criar a imagem Docker para a aplicação, enfrentamos dificuldades relacionadas à configuração do Dockerfile. O principal problema foi garantir que todas as dependências da aplicação fossem corretamente instaladas dentro do container, sem gerar conflitos ou falhas de execução. Além disso, a configuração das variáveis de ambiente, das credenciais do ambiente AWS e adaptação da estrutura de pastas da aplicação para funcionar no ambiente do container foram desafios adicionais, resultando em falhas na execução inicial. Esse processo demandou diversos ajustes e testes até que a imagem fosse gerada corretamente e a aplicação funcionasse como esperado no ambiente Docker.

## ⚖️ Licença
Este projeto é protegido por uma Licença Proprietária. Todos os direitos reservados.

O uso, modificação e distribuição deste software são estritamente proibidos sem a autorização.

<img src="https://badgen.net/badge/License/Proprietary License/gray?icon=github" alt="Status Badge"/>

## Responsáveis pelo desenvolvimento

 | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/109036881?v=4" width=115><br><sub>Alexander Júnior</sub>](https://github.com/alexanderjr02) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/64118446?v=4" width=115><br><sub>Gerson Ramos</sub>](https://github.com/gersonlramos) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/173846137?v=4" width=115><br><sub>Jeff Carneiro</sub>](https://github.com/j3ffcarneiro) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/173844938?v=4" width=115><br><sub>Lizandra Resende</sub>](https://github.com/ResendeLiz) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/101699095?v=4" width=115><br><sub>Nathalia Reis</sub>](https://github.com/NathaliaOSReis)
| :---: | :---: | :---: | :---: | :---: |

