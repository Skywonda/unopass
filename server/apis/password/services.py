from typing import List
from fastapi import Depends, HTTPException, status

from server.apis.password.repository import PasswordRepository
from server.apis.password.schemas import CreatePassword
from server.apis.password.models import Password
from server.apis.password.schemas import ShowPassword
from server.apis.user.repositories import UserRepository


class PasswordServices:
    """
    Business Logic for users password
    """
    def __init__(self, password_repository : PasswordRepository = Depends(), user_repository : UserRepository = Depends()):
        self.password_repository = password_repository
        self.user_repository = user_repository
    def save_password(self, password : CreatePassword, owner_id : int) -> Password:
        existing_platfrom = self.password_repository.get_password_by_platfrom(password.platform )
        existing_id = self.user_repository.get_by_id(user_id=owner_id)
        if not existing_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="owner does not exist!")
        if existing_platfrom:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="password for the platform already exist!")
        return self.password_repository.save_password(password = password, owner_id=owner_id)

    def get_list_of_user_password(self, owner_id : int) -> List[Password]:
        passwords = self.password_repository.get_list_of_user_passwords(owner_id)
        return passwords
    
    def get_password_by_platform(self, platform) -> ShowPassword:
        password = self.password_repository.get_password_by_platfrom(platform)
        return password

    def update_password_by_id(self, id: int, password : CreatePassword, owner_id):
        action = self.password_repository.edit_password(id = id , password = password, owner_id = owner_id)
        if not action:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with id {id} not found")
        return action