from time import gmtime, strftime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Incidence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fk_disease = db.Column(db.Integer, nullable=False)
    fk_user = db.Column(db.Integer, nullable=False)
    incidenceDate = db.Column(db.DateTime(), nullable=False)
    created_at = db.Column(db.DateTime(), default=strftime("%Y-%m-%d"))
    updated_at = db.Column(db.DateTime(), default=strftime("%Y-%m-%d"))