from myapp import db


class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    display_name = db.Column(db.String(50))
    email = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(128),nullable=False)
    address = db.Column(db.String(128))
    phone = db.Column(db.String(20))
