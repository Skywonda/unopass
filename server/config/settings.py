from decouple import config


class Setting:
    # PROJECT
    PROJECT_NAME = config("PROJECT_NAME")
    PROJECT_VERSION = config("PROJECT_VERSION")

    POSTGRES_USER = config("POSTGRES_USER")
    POSTGRES_DATABASE = config("POSTGRES_DATABASE")
    POSTGRES_PASSWORD = config("POSTGRES_PASSWORD")
    POSTGRES_HOST = config("POSTGRES_HOST")
    POSTGRES_PORT = config("POSTGRES_PORT")
    DATABASE_URL = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"
    )


settings = Setting()
