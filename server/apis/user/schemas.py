from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    password: str


class CreateUser(UserBase):
    class Config:
        extra_schema = {
            "example": {
                "name": "unopass",
                "email": "no-reply@unopass.com",
                "password": "password"
            }
        }


class ReadUser(UserBase):
    id : int
    class Config:
        orm_mode = True
