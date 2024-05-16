from app import db
import uuid

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(100), primary_key=True, default=str(uuid.uuid4()), unique=True)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    type_document = db.Column(db.Integer, db.ForeignKey("types_document.id"), nullable=False)
    document = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.VARBINARY(256), nullable=False)
    role = db.Column(db.Integer, db.ForeignKey("roles.id"))
    vote = db.Column(db.String(100))


    Type_document = db.relationship("Type_document")
    Role = db.relationship("Role")
    Session = db.relationship("Session")

    def to_dict(self):
        user = {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "email": self.email,
            "type_document": self.type_document,
            "document": self.document,
            "phone": self.phone,
            "role": self.role,
            "vote": self.vote,
            "Role": self.Role.to_dict(),
            "Type_document": self.Type_document.to_dict(),
        }
        return user