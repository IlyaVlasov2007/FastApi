from database.session_manager import Manager
from models.models import Article
from schemas.article import UpdateArticle  # локальный импорт, чтобы избежать циклов


class ArticleManager:

    def __init__(self):
        self.manager = Manager()

    def get_articles(self, skip: int = 0, limit: int = 100) -> list[Article]:
        """Метод получает объекты из базы данных\n
        Параметры:
            - skip (int, optional): Количество записей для пропуска (пагинация). 
            По умолчанию 0.
            - limit (int, optional): Максимальное количество возвращаемых записей. 
            По умолчанию 100.
        Метод возвращает список объектов из БД"""

        with self.manager.get_session() as session: 
            return session.query(Article).offset(skip).limit(limit).all()


    def create_article(self, article: Article) -> Article:
        """Метод создает объект в базе данных\n
        Параметры:
            - article: объект, который необходимо добавить\n
        Метод добавит объект и вернет его же"""

        with self.manager.get_session() as session:
            session.add(article)
            session.commit()

            return article


    def update_article(self, id: int, updated_article: 'UpdateArticle') -> Article | None:
        """Метод обновляет объект в базе данных\n
        Параметры:
            - id (int): ID статьи в БД\n
            - updated_article: изменённая схема (Pydantic)\n
        Если объект с таким id есть, то метод обновит его и вернет обновленный объект,
        иначе вернет None"""

        with self.manager.get_session() as session:
            article = session.query(Article).get(id)
            if not article:
                return None
            data = updated_article.dict(exclude_unset=True)
            for key, value in data.items():
                if key != 'id' and value is not None:
                    setattr(article, key, value)
            session.commit()
            session.refresh(article)
            return article
            

    def delete_article(self, id: int) -> Article | None:
        """Метод удаляет объект из базы данных\n
        Параметры:
            - id (int): ID записи в БД\n
        Если объект с таким id есть, то метод удалит его и вернет объект,
        иначе вернет None"""

        with self.manager.get_session() as session:
            article = session.query(Article).get(id)

            if not article:
                return None
            
            session.delete(article)
            session.commit()

            return article