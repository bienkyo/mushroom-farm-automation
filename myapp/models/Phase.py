from myapp import db


class Phase(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    n_days = db.Column(db.Integer)
    nth_phase = db.Column(db.Integer)

    mushroom_color = db.Column(db.String(50))
    avg_weight_per_seed = db.Column(db.Integer)
    n_alive = db.Column(db.Integer)
    n_dead = db.Column(db.Integer)

    mushroom_id = db.Column(db.Integer, db.ForeignKey('mushroom.id'))
    crop_id = db.Column(db.Integer, db.ForeignKey('crop.id'))
    material_id = db.Column(db.Integer, db.ForeignKey('material.id'))

    material = db.relationship('Material', backref='phase', uselist=False, lazy=True)
    mushroom_conditions = db.relationship('MushroomCondition', backref='phase', lazy=True)
