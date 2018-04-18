from myapp import db


class Mushroom(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    kingdom = db.Column(db.String(50))
    division = db.Column(db.String(50))
    _class = db.Column(db.String(50))
    family = db.Column(db.String(50))
    genus = db.Column(db.String(50))
    spieces = db.Column(db.String(50))
    common_name = db.Column(db.String(50))
    number_of_phase = db.Column(db.Integer)

    phases = db.relationship('Phase', backref='mushroom', lazy=True)
