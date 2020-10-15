import os

from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv
from werkzeug.middleware.proxy_fix import ProxyFix

from src.controller.teste import bp
from src.controller.account.accountController import accountBp
from src.controller.dashboard.dashBoardController import dashBp
from src.controller.disease.diseaseController import diseaseBp

from src.model.userModel import db as user_db
from src.model.diseaseModel import db as disease_db

load_dotenv(find_dotenv())

try:
    template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    template_dir = os.path.join(template_dir, 'repo')
    template_dir = os.path.join(template_dir, 'src')
    template_dir = os.path.join(template_dir, 'view')
    
    app = Flask(__name__, template_folder=template_dir, static_folder=template_dir)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://application:123456@127.0.0.1:3306/epidemiapp'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    
    app.secret_key = b'teste'

    user_db.init_app(app)
    disease_db.init_app(app)

    app.wsgi_app = ProxyFix(app.wsgi_app)
    
    app.register_blueprint(bp)
    app.register_blueprint(accountBp)
    app.register_blueprint(dashBp)
    app.register_blueprint(diseaseBp)

except Exception as error:
    print(f'Erro: {error}')

@app.route('/')
def index():
    return render_template('Home/home.html', title='Home')