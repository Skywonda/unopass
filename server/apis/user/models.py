from server.config.database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String)
    user_saved_passwords = relationship("Password", back_populates = "owner")

    def __repr__(self):
        return f"id : {self.id}, name : {self.name}, email : {self.email}, password : {self.password}"
