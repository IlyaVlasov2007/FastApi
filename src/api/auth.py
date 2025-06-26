from fastapi import APIRouter, HTTPException, Response, Request
from fastapi.responses import RedirectResponse
from api.auth_config import security, config

from schemas.user import User, UserLogin 
from models.models import User as _User
from database.user_manager import UserManager

manager = UserManager()

auth_router = APIRouter(tags=['Аутентификация'])


@auth_router.post('/create_user', summary='Создать пользователя')
def create_user(new_user: User, auth: bool = True) -> User:
    user = _User(**new_user.model_dump())
    user_id = manager.create_user(user=user).id

    if auth: 
        return RedirectResponse(url=f'/auth/{user_id}', status_code=307)
    
    return user_id


@auth_router.post('/auth/{id}', summary='Авторизация', response_model=None)
def get_access_token(id: int, response: Response):
    user = manager.get_user_by_id(id=id)

    if not user:
        raise HTTPException(status_code=404, detail='User not exists')
    
    token = security.create_access_token(uid=str(id))
    response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)

    return {'success': True}


@auth_router.post('/login', summary='Войти в аккаунт')
def login(user: UserLogin, response: Response):
    print(user.login)
    user_id = manager.get_user_id_by_login(login=user.login)
    print(user_id)
    print(user)

    if manager.check_user_data(user):
        return RedirectResponse(url=f'/auth/{user_id}', status_code=307)
    
    raise HTTPException(status_code=404, detail='Invalid register data')

