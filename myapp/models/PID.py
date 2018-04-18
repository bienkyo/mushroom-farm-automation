from myapp import db


class PID(db.Model):
    __tablename__ = 'pid'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    direction = db.Column(db.String(10))  # raise, lower or both
    band = db.Column(db.Float, default=0)
    max_measure_age = db.Column(db.Integer, default=120)
    is_activated = db.Column(db.Boolean, default=True)
    period = db.Column(db.Integer, default=30)
    setpoint = db.Column(db.Float, default=30.0)
    p = db.Column(db.Float, default=1.0)  # Kp gain
    i = db.Column(db.Float, default=0.0)  # Ki gain
    d = db.Column(db.Float, default=0.0)
    integrator_min = db.Column(db.Float, default=-100.0)
    integrator_max = db.Column(db.Float, default=100.0)
    raise_min_duration = db.Column(db.Float, default=0.0)
    raise_max_duration = db.Column(db.Float, default=0.0)
    raise_min_off_duration = db.Column(db.Float, default=0.0)
    lower_min_duration = db.Column(db.Float, default=0.0)
    lower_max_duration = db.Column(db.Float, default=0.0)
    lower_min_off_duration = db.Column(db.Float, default=0.0)
