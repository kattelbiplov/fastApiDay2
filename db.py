from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABE_URL = "mysql+pymysql://root:password@localhost:3306/studentrecord"
engine = create_engine(SQLALCHEMY_DATABE_URL)

SessionLocal = sessionmaker(bind= engine, autocommit=False, autoflush=False, )


Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()