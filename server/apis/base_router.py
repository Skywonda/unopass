from fastapi import APIRouter

from server.apis.user.routers import router as UserRouter

router = APIRouter(prefix="/tester")
router.include_router(UserRouter, prefix="/user", tags=["user"])
