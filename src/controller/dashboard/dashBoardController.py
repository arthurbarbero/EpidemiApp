from flask import Blueprint, current_app, render_template, request, Response, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

dashBp = Blueprint('dash', __name__, url_prefix='/dash')

@dashBp.route('/')
def dashIndex():
    return render_template('DashBoard/dashboard.html', title='Doênças', data={"logado": True})
