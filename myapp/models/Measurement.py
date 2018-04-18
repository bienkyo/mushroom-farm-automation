from myapp import db


class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    unit = db.Column(db.String(10))

