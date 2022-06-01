from typing_extensions import Self
from server.config.database import Base
from sqlalchemy import Column, String, Integer


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String)

    def __repr__(self):
        return f"id : {self.id}, name : {self.name}, emai : {self.email}"
