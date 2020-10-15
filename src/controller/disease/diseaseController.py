from flask import Blueprint, current_app, render_template, request, Response, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

diseaseBp = Blueprint('disease', __name__, url_prefix='/disease')

@diseaseBp.route('/')
def diseaseIndex():
    return render_template('Disease/disease.html', title='Cadastrar Doenças', data={"logado": True})

@diseaseBp.route('/register')
def diseaseRegister():
    return Response('ok')