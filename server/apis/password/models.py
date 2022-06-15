from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from  server.config.database import Base
from server.apis.password.schemas import ShowPassword

class Password(Base):
    __tablename__ = "passwords"
    id = Column(Integer, primary_key = True,  index = True)
    platform = Column(String, nullable = False)
    username = Column(String, nullable = True)
    password = Column(String, nullable = False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates = "user_saved_passwords")

    def __repr__(self) -> ShowPassword:
        return f"id : {self.id}, platform : {self.platform}, username : {self.username}, password : {self.password} , owner_id : {self.owner_id}"