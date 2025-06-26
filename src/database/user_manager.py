from database.session_manager import Manager
from models.models import User
from schemas.user import UpdateUser, UserLogin


class UserManager:

    def __init__(self):
        self.manager = Manager()

    
    def get_user_by_id(self, id: int) -> User:
        with self.manager.get_session() as session:
            return session.query(User).get(id)
    

    def get_user_id_by_login(self, login: str) -> int | None:
        with self.manager.get_session() as session:
            user = session.query(User).filter(User.login == login).first()
            return user.id if user else None


    def check_user_data(self, user: UserLogin):
        with self.manager.get_session() as session:
            return session.query(User).filter(User.login == user.login,
                                              User.password_hash == user.password_hash)\
                                              .first()


    def get_users(self, skip: int = 0, limit: int = 100) -> list[User]:
        """Метод получает объекты из базы данных\n
        Параметры:
            - skip (int, optional): Количество записей для пропуска (пагинация). 
            По умолчанию 0.
            - limit (int, optional): Максимальное количество возвращаемых записей. 
            По умолчанию 100.
        Метод возвращает список объектов из БД"""

        with self.manager.get_session() as session: 
            return session.query(User).offset(skip).limit(limit).all()


    def create_user(self, user: User) -> User:
        """Метод создает объект в базе данных\n
        Параметры:
            - User: объект, который необходимо добавить\n
        Метод добавит объект и вернет его же"""

        with self.manager.get_session() as session:
            session.add(user)
            session.commit()

            return user


    def update_user(self, id: int, updated_user: 'UpdateUser') -> User | None:
        """Метод обновляет объект в базе данных\n
        Параметры:
            - id (int): ID пользователя в БД\n
            - updated_user: изменённая схема (Pydantic)\n
        Если объект с таким id есть, то метод обновит его и вернет обновленный объект,
        иначе вернет None"""

        with self.manager.get_session() as session:
            user = session.query(User).get(id)

            if not user:
                return None
            
            data = updated_user.model_dump(exclude_unset=True)
            
            for key, value in data.items():
                if key != 'id' and value is not None:
                    setattr(user, key, value)

            session.commit()
            session.refresh(user)
            
            return user
            
    
    def delete_user(self, id: int) -> User | None:
        """Метод удаляет объект из базы данных\n
        Параметры:
            - id (int): ID пользователя в БД\n
        Если объект с таким id есть, то метод удалит его и вернет объект,
        иначе вернет None"""

        with self.manager.get_session() as session:
            user = session.query(User).get(id)

            if not user:
                return None
            
            session.delete(user)
            session.commit()

            return user