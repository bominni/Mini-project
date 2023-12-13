from pydantic import BaseModel, EmailStr
class Signup_user(BaseModel):
    age: int
    username: str
    email: EmailStr
    password: str

class UserSignIn(BaseModel):
    email: EmailStr
    password: str
