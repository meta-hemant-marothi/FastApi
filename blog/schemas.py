from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    class config:
        orm_mode = True
    name: str
    email: str
