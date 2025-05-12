from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


class ShowUser(User):
    username: str
    password: str
    amount: float