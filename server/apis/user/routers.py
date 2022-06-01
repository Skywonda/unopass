from typing import List
from fastapi import Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from .schemas import ReadUser, CreateUser
from .services import UserServices

router = InferringRouter()


@cbv(router)
class UserRouter:
    """
    This is class is responsible for routing all requests from user
    """

    def __init__(self, user_services: UserServices = Depends()):
        self.user_services = user_services

    @router.post("/create", response_model=ReadUser, status_code=201)
    def create(self, create: CreateUser):
        """
        Create a new user
        """
        return self.user_services.create_user(create)

    @router.get("/", response_model=List[ReadUser], status_code=201)
    def get_all_user(self):
        """
        Get all users
        """
        return self.user_services.get_all_users()
