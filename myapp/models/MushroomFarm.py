from myapp import db


class FarmSensor(db.Model):
    n_sensors = db.Column(db.Integer, default=1)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'), primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey('mushroom_farm.id'), primary_key=True)


class MushroomFarm(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
    status_code = db.Column(db.Integer, db.ForeignKey('status.status_code'))
    address = db.Column(db.String(128))

    n_sensors = db.relationship('FarmSensor', backref='mushroom_farm', primaryjoin=id == FarmSensor.farm_id)

