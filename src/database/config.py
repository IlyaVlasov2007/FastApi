from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DB_URL = 'sqlite:///news.db'
engine = create_engine(url=DB_URL)

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
