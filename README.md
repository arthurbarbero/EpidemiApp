Arthur Barbero - RA 1460481821009

#https://youtu.be/Wcw4ZTJPn18

## Primeira entrega
-----

### Como iniciar o projeto

- Clone o projeto usando o comando 
  
  ```
    git clone https://github.com/arthurbarbero/arthurbarbero.git
    
    cd arthurbarbero

    git fetch & git checkout primeira-entrega
  ```

- Criando e acessando o Virtual Enviroment:
  ```
    python -m venv env

    cd env/Scripts
    
    activate
  ``` 

- Volte para a raiz da pasta e instale as dependências:
  ``` 
    pip install -r requirements.txt
  ```

- Após instalar as dependências, inicie a aplicação Flask:
  ```
    python src/main.py
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
