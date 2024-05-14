from app import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50))
    users = db.relationship('User')