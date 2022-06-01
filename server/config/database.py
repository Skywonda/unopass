from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

from server.config.settings import settings

Base = declarative_base()

db_url = settings.DATABASE_URL

engine = create_engine(db_url)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def init_db():
    import server.base_model

    Base.metadata.create_all(bind=engine)
