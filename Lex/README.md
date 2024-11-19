
# Configurações de Ambiente na AWS

Esse projeto trata das configurações de ambientes dentro da AWS para que seja possível realizar o deploy da aplicação. 

# Tecnologias utilizadas

![AWS Lambda](https://img.shields.io/badge/AWS_Lambda-orange?logo=amazonaws&logoColor=white)
![Amazon S3](https://img.shields.io/badge/Amazon_S3-orange?logo=amazonaws&logoColor=white)
![Amazon DynamoDB](https://img.shields.io/badge/Amazon_DynamoDB-blue?logo=amazonaws&logoColor=white)
![Amazon Polly](https://img.shields.io/badge/Amazon_Polly-232F3E?logo=amazonaws&logoColor=white)
![Amazon Transcribe](https://img.shields.io/badge/Amazon_Transcribe-FF9900?logo=amazonaws&logoColor=white)
![Amazon Lex](https://img.shields.io/badge/Amazon_Lex-00A3E0?logo=amazonaws&logoColor=white)
![Amazon Rekognition](https://img.shields.io/badge/Amazon_Rekognition-527FFF?logo=amazonaws&logoColor=white)
![Amazon Bedrock](https://img.shields.io/badge/Amazon_Bedrock-FF4F8B?logo=amazonaws&logoColor=white)

# Estrutura das pastas
```
Lex/
├── Bot_Final/
│   ├── DengueBot_FINAL.zip
│   ├── DengueBot_v7.zip
│   └── Lex_FINAL.zip
│
├── Lex_Antigos/
│   ├── DengueBot_v2.zip
│   ├── DengueBot_v3.zip
│   ├── DengueBot_v4.zip
│   ├── DengueBot_v5.zip
│   └── DengueBot_v6.zip
│
└── Lambda/
    ├── bedrock.py
    ├── contato.py
    ├── denunciaFoto.py
    ├── detectaSintoma.py
    ├── dicasDetect.py
    ├── dicasPrevencao.py
    ├── dicasTratamento.py
    ├── dicionarioDicas.py
    ├── infereSintomas.py
    ├── lambda_function.py
    ├── rekognition.py
    └── saudacaoes.py
```

# Configurações de ambiente e deploy:

Para que seja possível realizar a configuração do seu ambiente AWS será necessário:

1. **Conta ativa na AWS:** Caso ainda não possua, será necessário [criar uma conta](https://docs.aws.amazon.com/pt_br/accounts/latest/reference/manage-acct-creating.html) e configurá-la conforme o link indicado.

2. **Configuração do Amazon S3:** No console da AWS, vá para a página do S3 e [crie dois buckets](https://docs.aws.amazon.com/pt_br/AmazonS3/latest/userguide/create-bucket-overview.html) – um para armazenar imagens e outro para áudios. Os nomes dos buckets devem ser distintos, e é importante configurar o acesso do bucket para que seja público.

3. **Configuração do DynamoDB:** Acesse a página do DynamoDB e [crie uma tabela](https://docs.aws.amazon.com/pt_br/amazondynamodb/latest/developerguide/SettingUp.DynamoWebService.html). Escolha um nome para a tabela e, no campo *Chave de Partição*, insira `unique_id` (String).

4. **Acesso ao Amazon Bedrock:** Na página do [Amazon Bedrock](https://console.aws.amazon.com/bedrock/), [solicite acesso ao modelo Titan](https://docs.aws.amazon.com/pt_br/bedrock/latest/userguide/getting-started.html) da Amazon.

5. **Preparação dos arquivos:** No repositório do GitHub, salve os arquivos `Lambda_Final`, `Lex_Final` e `Lib-Requests` em sua máquina.

6. **Configuração da função Lambda:** No console do Lambda, [crie uma nova função](https://docs.aws.amazon.com/pt_br/lambda/latest/dg/configuration-function-zip.html). Selecione Python 3.12 no campo de Tempo de Execução e faça o upload do arquivo `.zip` `Lambda_Final` para que a função esteja disponível.

7. **Ajuste do código Lambda:** Na aba *Código* da função Lambda, localize a linha 64 do arquivo `denunciaFoto.py` e altere o nome da variável `bucket_name` para o nome do bucket criado no passo 2, responsável pelo armazenamento das imagens:

   ```python
   bucket_name = "INSIRA_NOME_DA_SUA_BUCKET"
    ```
8. **Deploy da função**: Faça o deploy do código.
9. **Configuração de Timeout**: Na aba _Configurações_, edite o _Tempo Limite_ da função Lambda para 45 segundos..
10. **Criação de camada Lambda**: Ainda na função Lambda, crie uma nova [camada](https://docs.aws.amazon.com/pt_br/lambda/latest/dg/chapter-layers.html) e faça o upload do arquivo `Lib-Requests`. Lembre-se de que o _Tempo de Execução_, deve ser o mesmo da sua função Lambda.
11. **Configurações de permissões no IAM**: No console do [IAM](https://console.aws.amazon.com/iam/), vá até a aba _Funções_, localize a função Lambda recém-criada e acesse _Permissões > Adicionar Permissões_ e [adicione permissões](https://docs.aws.amazon.com/pt_br/lambda/latest/dg/lambda-permissions.html) para os seguintes serviços: _S3, Polly, Transcribe, Translate, LexV2, Rekognition, Bedrock._
12. **Configuração do Amazon Lex**: Acesse o console do [Amazon Lex](https://console.aws.amazon.com/bedrock/) e [importe](https://docs.aws.amazon.com/pt_br/lex/latest/dg/import-export.html) o arquivo `Lex_Final`, Defina o nome do bot, selecione a primeira opção em Permissões _IAM_, marque "não" em _COPPA_ (Children’s Online Privacy Protection Act) e clique em _Criar_.
13. **Construção do Bot**: Após a importação, selecione o bot importado, acesse a barra lateral direita, vá em _Intents_, e clique em _Build_ no canto superior direito para compilar o bot. 
14. **Criação da versão do bot**: Na barra lateral esquerda, acesse _Bot Versions_ e crie uma nova versão do bot que você acabou de compilar.
15. **Configuração de Alias**: Acesse _Deployment > Aliases_, clique em _Criar Alias_, escolha um nome e selecione a versão do bot criada no passo anterior. Em seguida, clique em _Criar_.
16. **Configuração de idioma e Lambda do bot**: Após a criação do alias, clique nele. Em _Languages_, selecione _Português (Brazil)_. Na janela _Lambda Function_, escolha a função Lambda criada no passo 6 e clique em _Salvar_.
17. **Registro de ID**: Anote o número do ID do Alias e também o ID do Bot, pois ambos serão necessários no arquivo `app.py` que está no diretório do projeto.
