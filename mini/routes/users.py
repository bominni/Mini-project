from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

user_router = APIRouter()

users = {}

@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail="이미 등록된 이메일이 있습니다."
        )
    users[data.email] = data
    print(users, "users")
    return {
        "message": "회원가입에 성공했습니다."
    }

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if user.email not in users or users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="이메일 또는 비밀번호를 다시 확인해주세요."
        )
    return {
        "message": "로그인 성공했습니다."
    }