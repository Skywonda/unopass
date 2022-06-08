from pydantic import BaseModel


class CreatePassword(BaseModel):
    platform : str
    username : str
    password : str

class ShowPassword(BaseModel):
    id : int
    platform : str
    username : str
    password : str 
    class Config:
        orm_mode = True

class EditPassword(BaseModel):
    username : str
    password : str