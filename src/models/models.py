from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from datetime import datetime

from database.config import Base


class Article(Base):
    __tablename__ = 'articles'

    id: int = Column(Integer, primary_key=True)

    title: str = Column(String(250), nullable=False)
    description: str = Column(String)
    created_at: datetime = Column(DateTime, nullable=False, default=datetime.now)
    updated_at: datetime = Column(DateTime, default=None, onupdate=datetime.now)

    author_id: int = Column(Integer, ForeignKey('users.id'), nullable=False)


class User(Base):
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)

    login: str = Column(String, nullable=False, unique=True)
    password_hash: str = Column(String, nullable=False)
    role: int = Column(Integer, nullable=False, default=1)

    articles = relationship('Article', backref='article', cascade='all, delete')