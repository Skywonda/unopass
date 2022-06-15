from requests import delete
from sqlalchemy.orm import Session
from fastapi import Depends

from server.apis.dependencies import get_db
from server.apis.password.schemas import CreatePassword, EditPassword, ShowPassword
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

    def get_password_by_platfrom(self, platform : str, owner_id : int) -> Password:
        password = self.db.query(Password).filter(Password.platform == platform, Password.owner_id == owner_id).first()
        return password

    def get_list_of_user_passwords(self, owner_id) -> Password:
        list_of_passwords = self.db.query(Password).filter(Password.owner_id == owner_id).all()
        return list_of_passwords

    def edit_password(self, password : EditPassword, owner_id : int, platform : str) -> None:
        existing_password = self.db.query(Password).filter(Password.platform == platform, Password.owner_id == owner_id)
        if not existing_password:
            return 0
        existing_password.update(password.__dict__)
        self.db.commit()
        return existing_password.first()

    def delete_password(self, platform : str, owner_id : int):
        existing_password = self.db.query(Password).filter(Password.owner_id == owner_id, Password.platform == platform).first()
        if not existing_password:
            return 0
        self.db.delete(existing_password)
        self.db.commit()
        return "succesful"
    