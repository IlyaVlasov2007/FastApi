from fastapi import APIRouter, HTTPException

from schemas.user import User, UpdateUser
from models.models import User as _User

from database.user_manager import UserManager


manager = UserManager()

user_router = APIRouter(prefix='/user', tags=['Пользователи'])


@user_router.get('/', summary='Получить пользователей')
def get_users() -> list[User]:
    return manager.get_users()


@user_router.post('/', summary='Создать пользователя')
def create_user(new_user: User) -> User:
    user = _User(**new_user.model_dump())
    manager.create_user(user=user)

    return user


@user_router.put('/{id}', summary='Изменить пользователя')
def update_user(id: int, updated_user: UpdateUser) -> User:
    user = manager.update_user(id=id, updated_user=updated_user)
    if user is None:
        raise HTTPException(status_code=404, detail='Пользователь не найден')
    return user


@user_router.delete('/{id}', summary='Удалить пользователя')
def delete_user(id: int) -> User:
    deleted_user = manager.delete_user(id=id)

    return deleted_user