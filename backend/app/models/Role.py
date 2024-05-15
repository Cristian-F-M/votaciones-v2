from app import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50))


    def to_dict(self):
        role = {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
        return role