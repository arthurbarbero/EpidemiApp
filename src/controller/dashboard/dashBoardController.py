from flask import Blueprint, current_app, render_template, request, Response, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

from src.controller.disease.diseaseController import getAllDisease
from src.controller.incidence.incidenceController import getAllIncidencesByDisease

dashBp = Blueprint('dash', __name__, url_prefix='/dash')

@dashBp.route('/', methods=["GET"])
def dashIndex():
    try:
        diseases = getAllDisease().json
        diseasesTable = getAllIncidencesByDisease()
    except Exception as error:
        print(error)
        diseases = []
        diseasesTable = []

       
    

    return render_template('DashBoard/dashboard.html', title='Doênças', data={"logado": True, "diseases": diseases, "diseasesTable": diseasesTable})
