from web import db
from web.app.models.base import Base


class User(Base):
    __tablename__ = "user"

    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, email: str, password: str):
        super().__init__()
        self.email = email
        self.password = password

    def json(self):
        return {
            "email": self.email,
            "password": self.password,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

