
from flask import Blueprint, current_app
from src.model.userModel import User as UserModel

bp = Blueprint('teste', __name__, url_prefix='/teste')

@bp.route('/')
def teste():
    teste = UserModel.query.all()
    print(teste[0].name)

    return '<h1>Hello, World!</h1>'
