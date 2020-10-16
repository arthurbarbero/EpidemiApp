import json

from flask import Blueprint, current_app, render_template, request, Response, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

from src.model.incidenceModel import Incidence as IncidenceModel
from src.model.userModel import User as UserModel
from src.model.diseaseModel import Disease as DiseaseModel

incidenceBp = Blueprint('incidence', __name__, url_prefix='/incidence')

@incidenceBp.route('/')
def incidenceIndex():
    return render_template('Incidence/incidence.html', title='Cadastrar incidência epidemiológica', data={"logado": True})

@incidenceBp.route('/register', methods=["POST", "GET"])
def incidenceRegister():
    try:
        db = SQLAlchemy(current_app)

        obj = request.json

        user = UserModel.query.filter_by(id=obj['user_id']).first()
        disease = DiseaseModel.query.filter_by(name=obj['selectedDisease']).first()
        newIncidence = IncidenceModel(fk_doenca=disease.id, fk_user=user.id, incidenceDate=obj['incidenceDate'])
        
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