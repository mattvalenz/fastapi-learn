from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:123456@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()