from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <h1>
        <p>EpidemiApp - Sistema de Coleta e Visualização de Dados Epidemiológicos</p>
        <p>Arthur Barbero - RA 1460481821009</p>
        <p>Fabrício Galende Marques de Carvalho</p>
    </h1>
    '''

if __name__ == "__main__":
    app.run()