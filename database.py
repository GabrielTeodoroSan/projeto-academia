from sqlalchemy.orm import sessionmaker, declarative_base 
from sqlalchemy import create_engine 


SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

