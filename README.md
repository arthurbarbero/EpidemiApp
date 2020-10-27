Arthur Barbero - RA 1460481821009

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

- Após instalar as dependências e criar o arquivo ``.env``, inicie a aplicação Flask:
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
