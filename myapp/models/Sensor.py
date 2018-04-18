from myapp import db
from myapp.models.MushroomFarm import FarmSensor

functions = db.Table('functions',
                     db.Column('sensor_id', db.Integer, db.ForeignKey('sensor.id'), primary_key=True),
                     db.Column('measurement_id', db.Integer, db.ForeignKey('measurement.id'), primary_key=True))


class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('sensor_manufacturer.id'))
    function_id = db.Column(db.Integer)
    power_supply = db.Column(db.Float)

    interface_id = db.Column(db.Integer, db.ForeignKey('sensor_interface.id'))

    functions = db.relationship('Measurement', secondary=functions, lazy='subquery',
                                backref=db.backref('sensors', lazy=True))

    n_sensors = db.relationship('FarmSensor', backref='sensor', primaryjoin=id == FarmSensor.sensor_id)


class SensorManufacturer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    country_code = db.Column(db.Integer, db.ForeignKey('country.id'))
    sensors = db.relationship('Sensor', backref='manufacturer')


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    country = db.relationship('SensorManufacturer', backref='country', uselist=False, lazy=True)


class SensorInterface(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))

    sensors = db.relationship('Sensor', backref='interface', lazy=True)
