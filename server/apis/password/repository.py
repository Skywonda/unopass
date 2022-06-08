from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List

from server.apis.dependencies import get_db
from server.apis.password.schemas import CreatePassword, ShowPassword
from server.apis.password.models import Password

class PasswordRepository:
    """
    This class is responsible for interacting with the password table in the database
    """
    def __init__(self, db : Session = Depends(get_db)):
        self.db = db

    def save_password(self, password : CreatePassword, owner_id : int) -> Password:
        db_password = Password(**password.dict(), owner_id = owner_id)
        self.db.add(db_password)
        self.db.commit()
        self.db.refresh(db_password)
        return db_password
    
    def get_password_by_platfrom(self, platform : str) -> Password:
        password = self.db.query(Password).filter(Password.platform == platform).first()
        return password

    def get_list_of_user_passwords(self, owner_id : int) -> List[Password]:
        list_of_passwords = self.db.query(Password).filter(Password.owner_id == owner_id).all()
        return list_of_passwords
    
    def edit_password(self,id : int, password : CreatePassword, owner_id) -> None:
        existing_password = self.db.query(Password).filter(Password.id == id)
        if existing_password:
            password.__dict__.update(owner_id=owner_id)
            existing_password.update(password.__dict__)
            self.db.commit()
            return 1
            