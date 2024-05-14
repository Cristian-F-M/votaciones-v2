from app import db
import uuid

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, default=str(uuid.uuid4()), unique=True)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    type_document = db.Column(db.Integer, db.ForeignKey("types_document.id"), nullable=False)
    document = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    role = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)
    vote = db.Column(db.Integer, db.ForeignKey("candidates.id"), nullable=False)



    Type_document = db.relationship("Type_document", backref="users")
    Role = db.relationship("Role", backref="users")