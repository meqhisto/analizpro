from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Gayrimenkul(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tip = db.Column(db.String(100))
    adres = db.Column(db.String(200))
    fiyat = db.Column(db.Float)

class Kullanici(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Diğer alanlar buraya gelecek

class Rapor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Diğer alanlar buraya gelecek