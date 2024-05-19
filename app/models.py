from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    waitlists = db.relationship('Waitlist', backref='user', lazy=True)

class Waitlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ticket_number = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='waiting')
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.now())
