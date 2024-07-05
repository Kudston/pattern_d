from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config import Settings

app_settings = Settings()

DB_USER=  "postgres"
DB_PASSWORD= "patternd"
DB_NAME=  "postgres"
DB_HOST=  "postgres"
DB_PORT=  "5432"

# SQL_ALCHEMY_DB_URL = app_settings.get_full_database_url()
data_base_full_url = app_settings.get_full_database_url()

engine = create_engine(data_base_full_url)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
