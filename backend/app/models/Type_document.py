from app import db

class Type_document(db.Model):
    __tablename__ = 'types_document'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(120))

    def to_dict(self):
        type_document = {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
        return type_document