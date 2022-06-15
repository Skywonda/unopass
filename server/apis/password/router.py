from typing import List
from typing_extensions import Self
from fastapi import APIRouter, Depends, status
from fastapi_utils.cbv import cbv

from server.apis.password.schemas import CreatePassword, EditPassword, ShowPassword
from server.apis.password.services import PasswordServices
from server.apis.user.models import User
from server.apis.login.router import get_current_from_token

router = APIRouter()

@cbv(router)
class PasswordRouter:
    """
    This class is responsible from routing all requsets from passwords
    """
    def __init__(self, password_services : PasswordServices = Depends(), current_user :User = Depends(get_current_from_token)):
        self.password_services = password_services
        self.current_user = current_user

    @router.post("/add/", response_model=ShowPassword, status_code=201)
    def save_password(self, password : CreatePassword):
        """
        Save new password from the user
        """
        return self.password_services.save_password(password= password, owner_id=self.current_user.id)

    @router.get("/", response_model=List[ShowPassword])
    def get_list_of_user_password(self):
        """
        Get list of user password
        """
        return self.password_services.get_list_of_user_password(self.current_user.id)

    @router.get("/{platform}")
    def def_password_by_platfrom(self, platform : str):
        return self.password_services.get_password_by_platform(platform, self.current_user.id)

    @router.put("/edit", response_model=ShowPassword)
    def edit_password(self, password : EditPassword, platform : str):
        return self.password_services.update_password_by_id(owner_id=self.current_user.id, password=password, platform=platform)

    @router.delete("/remove", status_code=status.HTTP_202_ACCEPTED)
    def delete_password(self, platform : str):
        return self.password_services.delete_password_by_platform(platform=platform, owner_id=self.current_user.id)