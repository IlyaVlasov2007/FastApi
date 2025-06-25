from fastapi import APIRouter, HTTPException

from schemas.article import Article, UpdateArticle
from models.models import Article as _Article

from database.article_manager import ArticleManager 


manager = ArticleManager()


article_router = APIRouter(prefix='/article', tags=['Новости'])

@article_router.get('/', summary='Получить новости')
def get_articles() -> list[Article]:
    return manager.get_articles()


@article_router.post('/', summary='Создать новость')
def create_article(new_article: Article) -> Article:
    article = _Article(**new_article.model_dump())
    manager.create_article(article=article)

    return article


@article_router.put('/{id}', summary='Изменить новость')
def update_article(id: int, updated_article: UpdateArticle) -> Article:
    article = manager.update_article(id=id, updated_article=updated_article)
    if article is None:
        raise HTTPException(status_code=404, detail='Новость не найдена')
    return article


@article_router.delete('/{id}', summary='Удалить новость')
def delete_article(id: int) -> Article:
    deleted_article = manager.delete_article(id=id)

    return deleted_article