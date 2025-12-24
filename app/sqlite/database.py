import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
load_dotenv()
SQLITE_DB = os.getenv("SQLITE_DB")

engine = create_engine(f"sqlite:///{SQLITE_DB}")
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
