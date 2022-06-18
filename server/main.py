from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from server.config.settings import settings
from server.apis.base_router import router
from server.config.database import init_db


def create_database():
    init_db()

def config_cor(app : FastAPI):
    app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def configure_router(app: FastAPI):
    app.include_router(router)


def start_server() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION
    )
    config_cor(app)
    configure_router(app)
    create_database()
    return app


app = start_server()


@app.get('/', tags=["Oops"])
def read_root():
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
