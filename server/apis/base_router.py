from fastapi import APIRouter

from server.apis.user.routers import router as UserRouter
from server.apis.password.router import router as PasswordRouter
from server.apis.login.router import router as LoginRouter

router = APIRouter(prefix="")
router.include_router(UserRouter, prefix="/user", tags=["user"])
router.include_router(PasswordRouter, prefix="/password", tags=["password"])
router.include_router(LoginRouter, prefix="/login", tags=["login"])