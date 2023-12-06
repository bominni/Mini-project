from pydantic import BaseModel, EmailStr
class User(BaseModel):
    age: int
    name: str
    email: EmailStr
    password: str

class UserSignIn(BaseModel):
    email: EmailStr
    password: str
