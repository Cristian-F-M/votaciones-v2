from app import db

class Type_document(db.Model):
    __tablename__ = 'types_document'
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50))