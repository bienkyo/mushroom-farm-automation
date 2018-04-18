from myapp import db


class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_time = db.Column(db.DateTime,nullable=False)
    end_time = db.Column(db.DateTime)
    note = db.Column(db.String(256))
    is_expr = db.Column(db.BOOLEAN,nullable=False)
    is_current = db.Column(db.Boolean, nullable=False)

    be_number = db.Column(db.Float)
    n_bags = db.Column(db.Integer)
    seed_ratio = db.Column(db.Float)

    mushroom_id = db.Column(db.Integer,db.ForeignKey('mushroom.id'))
    current_phase_id = db.Column(db.Integer,db.ForeignKey('phase.id'))
    