from myapp import db


class Status(db.Model):
    status_code = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(128))
    farms = db.relationship('MushroomFarm', backref='status', lazy=True)
