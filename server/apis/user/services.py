from fastapi import Depends
from fastapi import HTTPException, status
from typing import List

from .schemas import CreateUser, ReadUser
from .repositories import UserRepository
from .models import User


class UserServices:
    """
    Buisness logic for users
    """

    def __init__(self, user_repository: UserRepository = Depends()):
        self.user_repository = user_repository

    def create_user(self, create: CreateUser) -> User:
        """
        Create new user
        """
        existing_user = self.user_repository.get_by_email(create.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="This user already exist!"
            )
        return self.user_repository.user_create(create)

    def get_all_users(self) -> List[User]:
        """
        Get all users
        """
        return self.user_repository.get_all_user()
