from server.apis.dependencies import get_db
from .schemas import CreateUser
from .models import User

from fastapi import Depends
from typing import List
from sqlalchemy.orm import Session


class UserRepository:
    """
    This is a class reponsoble for interacting with the User table in the database
    """

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_all_user(self, limit: int = 10, skip: int = 0) -> List[User]:
        """
        Get all the user from the database
        """
        return self.db.query(User).limit(limit).offset(skip).all()

    def get_by_id(self, user_id) -> User:
        """
        Get users by id in the database
        """
        user = self.db.query(User).get(user_id)

    def get_by_email(self, user_email) -> User:
        """
        Get users by email from the database
        """
        user = self.db.query(User).filter(User.email == user_email).first()
        return user

    def user_create(self, create: CreateUser) -> User:
        """
        Get a new user in the database
        """
        db_user = User(**create.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
