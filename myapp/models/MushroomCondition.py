from myapp import db


class MushroomCondition(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    min_value = db.Column(db.Float, nullable=False)
    max_value = db.Column(db.Float, nullable=False)

    measurement_id = db.Column(db.Integer, db.ForeignKey('measurement.id'))
    phase_id = db.Column(db.Integer, db.ForeignKey('phase.id'))

    measurement = db.relationship('Measurement',uselist=False, backref='mushroom_condition', lazy=True)
