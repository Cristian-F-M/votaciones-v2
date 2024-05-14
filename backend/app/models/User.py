from app import db
import uuid

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(100), primary_key=True, default=str(uuid.uuid4()), unique=True)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    type_document = db.Column(db.String(100), db.ForeignKey("types_document.id"), nullable=False)
    document = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.String(50), nullable=False)
    password = db.Column(db.VARBINARY(256), nullable=False)
    role = db.Column(db.String(100), db.ForeignKey("roles.id"))
    vote = db.Column(db.String(100), db.ForeignKey("candidates.id"))



    Type_document = db.relationship("Type_document")
    Role = db.relationship("Role")