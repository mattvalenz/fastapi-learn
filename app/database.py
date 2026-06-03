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

##while True:

    # try:
    #     conn = psycopg2.connect(host = 'localhost', database='fastapi', user='postgres', password='123456', cursor_factory=RealDictCursor)
    #     cursor = conn.cursor()
    #     print("Database successfully connected.")
    #     break
    # except Exception as error:
    #     print("Connecting failed")
    #     print("Error:", error)
    #     time.sleep(2)