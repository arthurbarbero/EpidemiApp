# EpidemiApp :syringe::bar_chart:

## Devs :bust_in_silhouette:

 - Arthur Barbero [LinkedIn](https://www.linkedin.com/in/arthur-barbero/) / [Github](https://github.com/arthurbarbero);

## Objetivo :dart:

Este repositório tem como objetivo apresentar os conhecimentos adquiridos, de forma autodidática no que tange as ferramentas utilizadas abaixo, como a criação competa de uma simples aplicação web utilizando os conceitos de MVC em Python.

## Introdução :memo:

Com todos os acontecimentos decorrentes da pandemia, o mundo conseguiu ver a importância da coleta de dados e formulação das informações de forma coerente, não basta somente adquirir dados e também não basta apenas apresentar esses dados sem coêrencia. Tendo essa ideia em mente, o EpidemiApp nasce com a intenção de coletar e apresentar essas informações em uma aplicação Web.

## Tecnologias utilizadas :computer:

- [Python](https://www.python.org/);
- [Anaconda](https://www.anaconda.com/);
- [Flask](https://flask.palletsprojects.com/en/1.1.x/);
- [MariaDB](https://mariadb.org/).

## Features 

### Home :house:

Ao iniciar a aplicação Web, o usuário deverá se cadastrar ou se logar para iniciar o acesso a plataforma.

<img src="https://raw.githubusercontent.com/arthurbarbero/EpidemiApp/master/imagens/home.jpg" width="400">

### Login / Cadastre-se :pencil:

- Login:
<img src="https://raw.githubusercontent.com/arthurbarbero/EpidemiApp/master/imagens/Login.jpg" width="400">

- Cadastre-se:
<img src="https://raw.githubusercontent.com/arthurbarbero/EpidemiApp/master/imagens/Cadastro.jpg" width="400">

### DashBoard :chart_with_upwards_trend:

Após o Login, o usuário já pode ter uma análise de doênças cadastradas e a quantidade de suas incidências.

<img src="https://raw.githubusercontent.com/arthurbarbero/EpidemiApp/master/imagens/Dash.jpg" width="400">

### Cadastrar Doênça :pencil2:

O usuário poderá cadastrar a doênça para que todos possam informar quando houve incidência dessa doênça, ou nova doênça.
<img src="https://raw.githubusercontent.com/arthurbarbero/EpidemiApp/master/imagens/Cadastrar_doen%C3%A7a.jpg" width="400">

### Cadastrar Incidência da doênça :pill:

Utilizando das informações cadastradas de Doênça, o usuário informa quando houve mais uma incidência da doença selecionada.
<img src="https://raw.githubusercontent.com/arthurbarbero/EpidemiApp/master/imagens/Cadastrar_doen%C3%A7a.jpg" width="400">

### Gráfico de incidência :bar_chart:

Após todas informações cadastradas, o usuário pode visualizar graficamente para acompanhar o crescimento ou queda das incidências da doênça selecionada.
<img src="https://raw.githubusercontent.com/arthurbarbero/EpidemiApp/master/imagens/Incidencia.jpg" width="400">


### Requerimentos do projeto

- Python versão 3.6 ou maior - [Python Download](https://www.python.org/downloads/release/python-386/);
- [MariaDB](https://mariadb.com/downloads/)

### Como iniciar o projeto

- Clone o projeto usando o comando 
  
  ```
    git clone https://github.com/arthurbarbero/arthurbarbero.git
    
    cd arthurbarbero
    
    git checkout develop

    git pull
  ```

- Criando e acessando o Virtual Environment:
  ```
    python -m venv env

    env\Scripts\activate
  ``` 

- Instalando as dependências:
  ``` 
    pip install -r requirements.txt
  ```

- Criando o arquivo ``.env``

    Dentro da raiz do repositório existe um exemplo do arquivo ``.env`` chamado ``.env-example``, este deve ser seguido para a conecção com seu banco de dados local, segue exemplo 
  ```
    MARIA_DATABASE=epidemiapp
    MARIA_HOST=127.0.0.1
    MARIA_PORT=3306
    MARIA_USERNAME=application
    MARIA_PASSWORD=123456
  ```
    
    **Utilize usuário e senha com previlégios de administrador**
    
- Caso seja a primeira vez que irá rodar o projeto, inicialize o projeto com o seguinte comando:
  ```
    python wsgi.py init_db
  ```

- Para iniciar a aplicação Flask:
  ```
    python wsgi.py
  ```

- Assim que a seguinte mensagem aparecer, acesse o link informado para acessar a aplicação:
    ```
    * Serving Flask app "main" (lazy loading)
    * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    ```
