from myapp import db


class ControllerDevice(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    controller_type = db.Column(db.String(45))  # cluster or general

    farm_id = db.Column(db.Integer, db.ForeignKey('mushroom_farm.id'))
    pid_id = db.Column(db.Integer, db.ForeignKey('pid.id'))
    measurement_id = db.Column(db.Integer, db.ForeignKey('measurement.id'))

    pid = db.relationship('PID', backref='controller_device', uselist=False, lazy=True)
    measurement = db.relationship('Measurement', backref='controller_device', uselist=False, lazy=True)
