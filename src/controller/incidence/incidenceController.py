import json
from itertools import groupby

from flask import Blueprint, current_app, render_template, request, Response, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

from src.controller.disease.diseaseController import getAllDisease

from src.model.incidenceModel import Incidence as IncidenceModel
from src.model.userModel import User as UserModel
from src.model.diseaseModel import Disease as DiseaseModel

incidenceBp = Blueprint('incidence', __name__, url_prefix='/incidence')

@incidenceBp.route('/')
def incidenceIndex():
    try:
        diseases = getAllDisease().json
    except Exception as error:
        print(error)
        diseases = []

    return render_template('Incidence/incidence.html', title='Cadastrar incidência epidemiológica', data={"logado": True, "diseases": diseases})

@incidenceBp.route('/view/<disease>', methods=["GET"])
def incidenceView(disease):
    try:
        graphData = _getIncidenceByDisease(disease)
        diseases = getAllDisease().json
    except Exception as error:
        print(error)
        diseases = []

    return render_template('Incidence/incidenceView.html', title='Cadastrar incidência epidemiológica', data={"logado": True, "diseases": diseases, "graphs": graphData})

@incidenceBp.route('/register', methods=["POST", "GET"])
def incidenceRegister():
    try:
        db = SQLAlchemy(current_app)

        obj = request.json

        user = UserModel.query.filter_by(id=obj['user_id']).first()
        disease = DiseaseModel.query.filter_by(name=obj['selectedDisease']).first()
        newIncidence = IncidenceModel(fk_disease=disease.id, fk_user=user.id, incidenceDate=obj['incidenceDate'])
        
        with current_app.app_context():
            db.session.add(newIncidence)
            db.session.commit()

        res = json.dumps({'msg': 'Incidência cadastrada com sucesso!'})
        return Response(res, mimetype='application/json', status=200)
        
    except SQLAlchemyError as error:
        res = json.dumps({"Erro": str(error.__dict__['orig'])})
        return Response(res, mimetype='application/json', status=500)
    
    except Exception as error:
        res = json.dumps({"Erro": str(error)})
        return Response(res, mimetype='application/json', status=500)

def _getIncidenceByDisease(disease):
    try:
        db = SQLAlchemy(current_app)
        
        disease_id = DiseaseModel.query.filter_by(name=disease).first().id

        newIncidence = IncidenceModel.query.filter_by(fk_disease=disease_id).all()

        if not newIncidence:
            raise Exception('Não foram encontrados dados epidemiológicos para esta doênça.')

        if len(newIncidence) > 1:
            newIncidence = list(map(lambda x: {
                "disease" : disease,
                "incidenceDate":x.incidenceDate
                }, newIncidence))
            newIncidence = sorted(newIncidence, key=lambda i: i["incidenceDate"])
            newIncidence = [list(v) for k, v in groupby(newIncidence, key=lambda i: i["incidenceDate"])]
        else:
            newIncidence = [[{"disease" : disease,
                "incidenceDate":newIncidence[0].incidenceDate}]]

        return newIncidence

    except SQLAlchemyError as error:
        res = json.dumps({"Erro": str(error.__dict__['orig'])})
        return None
    
    except Exception as error:
        res = json.dumps({"Erro": str(error)})
        return None

def getAllIncidencesByDisease():
    try:
        db = SQLAlchemy(current_app)

        diseases = DiseaseModel.query.all()
        diseases = list(map(lambda x: {
                "id" : x.id,
                "name":x.name,
                "incidences": IncidenceModel.query.filter_by(fk_disease=x.id).count(),
                "lastIncidence": 
                    IncidenceModel.query.filter_by(fk_disease=x.id).order_by(IncidenceModel.incidenceDate.desc()).first().incidenceDate 
                        if IncidenceModel.query.filter_by(fk_disease=x.id).count() > 0 else 'Sem dados'
                }, diseases))

        return diseases

    except SQLAlchemyError as error:
        res = json.dumps({"Erro": str(error.__dict__['orig'])})
        return None
    
    except Exception as error:
        res = json.dumps({"Erro": str(error)})
        return None


def dateformat(value, format='%d/%m/%Y'):
    try:
        value = value.strftime(format)
        return value
    except Exception as error:
        return value

incidenceBp.add_app_template_filter(f=dateformat)