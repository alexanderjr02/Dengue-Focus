## <img src="../sprints-9-10-pb-aws-junho/assets/images/banner_denguebot.jpg" alt="Banner descritivo sobre o projeto" width="1250"/><br>
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

<img src="../sprints-9-10-pb-aws-junho/assets/videos/DengueGif.gif" alt="preview da aplicação" width="1250"/>

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

## 🏗️ Arquitetura da Aplicação

<img src="../sprints-9-10-pb-aws-junho/assets/images/Arquitetura_Aplicacao.jpg" alt="Arquitetura da aplicação" width="700"/>

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

