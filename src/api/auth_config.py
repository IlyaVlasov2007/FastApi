from fastapi import HTTPException, Response, Depends
from authx import AuthX, AuthXConfig

from schemas.user import User


config = AuthXConfig()

config.JWT_SECRET_KEY = 'SUPER_SECRET_KEY'
config.JWT_ACCESS_COOKIE_NAME = 'access_token'
config.JWT_TOKEN_LOCATION = ['cookies']

security = AuthX(config=config)
