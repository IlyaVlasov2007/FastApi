from api.article import article_router
from api.user import user_router
from api.auth import auth_router

from fastapi import APIRouter


main_router = APIRouter()

main_router.include_router(article_router)
main_router.include_router(user_router)
main_router.include_router(auth_router)