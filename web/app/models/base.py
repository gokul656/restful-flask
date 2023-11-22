from datetime import datetime

from ... import db


class Base(db.Model):
    __abstract__ = True
    __tablename__ = "base"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())

    def __init__(self,
                 created_at: datetime = datetime.now(),
                 updated_at: datetime = datetime.now()):
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def first(cls, *criterion):
        return cls.query.filter(criterion).first()

    @classmethod
    def exists(cls, *criterion) -> bool:
        return cls.query.filter(*criterion).scalar()

    def json(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
