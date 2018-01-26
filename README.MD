# Mathema API

## Configuração PyCharm

Verificar que a IDE PyCharm não está configurada para usar Virtual Environment:

* File -> Settings -> Project -> Project Interpreter

* Clique no ícone de chave inglesa, "Add local", menu esquerdo selecione System Interpreter, clique nas reticências e selecione o interpretador Python instalado em seu sistema

* Salve e feche

## Configuração Docker

* Clique com o botão direito no ícone do Docker, localizado na bandeja de notificações e selecione "Settings";

* Marque a opção "Expose daemon on..." e aguarde o serviço reiniciar;

* No menu esquerdo, selecione a opção "Shared Drives" e marque a opção correspondente ao drive que seu projeto se localiza;

* Aplique e feche as configurações;

## Configuração dos contêineres

 * No mesmo diretório do projeto, execute o comando `docker compose build` e aguarde a criação dos contêineres e instalação de dependências;

## Configuração do Django

É necessário efetuar migrações para criar o banco de dados conforme modelos criados, para isso, siga os passos:

* Conecte ao contêiner responsável por executar o Django, usando o comando `docker-compose run mathemaweb /bin/bash`;

* Dentro do shell do contêiner, execute os comandos padrões para configurar o Django: `python manage.py makemigrations`, `python manage.py migrate` e por fim `python manage.py createsuperuser` para criar o superusuário padrão;

* Saia do shell usando o comando `exit`.

## Iniciando o Django e Banco de Dados

Execute o comando `docker-compose up` no diretório do projeto e os contêineres serão iniciados. Após a configuração inicial descrita acima, só é necessário esse último comando para tornar o sistema operacional.
