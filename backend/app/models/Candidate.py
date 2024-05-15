from app import db
import uuid


class Candidate(db.Model):
    __tablename__ = "candidates"
    id = db.Column(
        db.String(100), primary_key=True, default=str(uuid.uuid4()), unique=True
    )
    user_id = db.Column(db.String(100), db.ForeignKey("users.id"), nullable=False)
    description = db.Column(db.String(100))
    photo = db.Column(db.String(100))


    def to_dict(self):
        candidate = {
            "id": self.id,
            "user_id": self.user_id,
            "description": self.description,
            "photo": self.photo,
            "User": self.User,
        }
        return candidate
