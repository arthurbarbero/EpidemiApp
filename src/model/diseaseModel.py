from time import gmtime, strftime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Disease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    symptoms = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=strftime("%Y-%m-%d"))
    update_at = db.Column(db.DateTime(), nullable=False, default=strftime("%Y-%m-%d"))