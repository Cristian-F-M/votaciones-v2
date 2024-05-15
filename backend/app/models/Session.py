from app import db


class Session(db.Model):
    __tablename__ = "sessions"
    id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)
    token = db.Column(db.String(255))
    expiration_date = db.Column(db.DateTime)

    def to_dict(self):
        session = {
            "id": self.id,
            "user_id": self.user_id,
            "token": self.token,
            "expiration_date": self.expiration_date,
        }
        return session
