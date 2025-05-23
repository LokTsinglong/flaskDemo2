from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy() 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    role= db.Column(db.String(50), nullable=False)  # 'admin','manager' or 'staff'