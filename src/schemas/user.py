from pydantic import BaseModel


class User(BaseModel):
    login: str
    password_hash: str
    role: int | None 


class UpdateUser(BaseModel):
    login: str | None 
    password_hash: str | None
    role: int | None
