import json

from flask import Blueprint, current_app, render_template, request, Response, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

from src.model.diseaseModel import Disease as DiseaseModel

diseaseBp = Blueprint('disease', __name__, url_prefix='/disease')

@diseaseBp.route('/')
def diseaseIndex():
    return render_template('Disease/disease.html', title='Cadastrar Doenças', data={"logado": True})

@diseaseBp.route('/register', methods=["POST", "GET"])
def diseaseRegister():
    try:
        db = SQLAlchemy(current_app)

        obj = request.json

        newDisease = DiseaseModel(**obj)
        
        with current_app.app_context():
            db.session.add(newDisease)
            db.session.commit()

        res = json.dumps({'msg': 'Doênça cadastrada com sucesso!'})
        return Response(res, mimetype='application/json', status=200)
        
    except SQLAlchemyError as error:
        res = json.dumps({"Erro": str(error.__dict__['orig'])})
        return Response(res, mimetype='application/json', status=500)
    
    except Exception as error:
        res = json.dumps({"Erro": str(error)})
        return Response(res, mimetype='application/json', status=500)


@diseaseBp.route('/getAllDisease', methods=["POST", "GET"])
def getAllDisease():
    try:
        db = SQLAlchemy(current_app)

        allDisease = DiseaseModel.query.all()

        allDisease = list(map(lambda x: x.name, allDisease))

        res = json.dumps(allDisease)
        return Response(res, mimetype='application/json', status=200)

    except SQLAlchemyError as error:
        res = json.dumps({"Erro": str(error.__dict__['orig'])})
        return Response(res, mimetype='application/json', status=500)
    
    except Exception as error:
        res = json.dumps({"Erro": str(error)})
        return Response(res, mimetype='application/json', status=500)
