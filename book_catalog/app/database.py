from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://database_url_9lr6_user:YEu0XfyJbD5s9wojs5F3kCCye7Rpr40V@dpg-crkif1btq21c73da4ncg-a.oregon-postgres.render.com/database_url_9lr6"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
