from typing import List
from fastapi import Depends, HTTPException, status

from server.apis.password.repository import PasswordRepository
from server.apis.password.schemas import CreatePassword, EditPassword
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
        user_passwords = self.password_repository.get_password_by_platfrom(owner_id=owner_id, platform=password.platform)
        if user_passwords:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="password for the platform already exist!")
        return self.password_repository.save_password(password = password, owner_id=owner_id)

    def get_list_of_user_password(self, owner_id) -> List[Password]:
        passwords = self.password_repository.get_list_of_user_passwords(owner_id=owner_id)
        return passwords

    def get_password_by_platform(self, platform, owner_id) -> ShowPassword:
        password = self.password_repository.get_password_by_platfrom(platform, owner_id)
        if not password:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This platform does not exist")
        return password

    def update_password_by_id(self, password : EditPassword, owner_id : int, platform : str):
        verify = self.get_password_by_platform(platform=platform, owner_id=owner_id)
        if not verify:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Password with {platform} not found")
        return self.password_repository.edit_password(password = password, owner_id = owner_id, platform=platform)
    
    def delete_password_by_platform(self, platform : str, owner_id : str):
        action = self.password_repository.delete_password(platform=platform, owner_id=owner_id)
        if not action:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{platform} not found")
        return action