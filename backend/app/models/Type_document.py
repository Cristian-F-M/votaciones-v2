from app import db

class Type_document(db.Model):
    __tablename__ = 'types_document'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50))
    users = db.relationship('User', backref='type_document', lazy=True)