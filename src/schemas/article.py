from pydantic import BaseModel


class Article(BaseModel):
    title: str
    description: str | None 
    author_id: int


class UpdateArticle(BaseModel):
    title: str | None 
    description: str | None 