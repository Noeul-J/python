from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.common.config import settings


SQLALCHENY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHENY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
