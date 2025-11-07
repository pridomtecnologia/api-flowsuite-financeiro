from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config


try:
    
    DATABASE_URL = config('DATABASE_URL')

    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine, autoflush=False)
    
except Exception as e:
    raise e

def get_db_session():
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()
