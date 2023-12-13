from fastapi import APIRouter, HTTPException, status, Depends
from models.users import Signup_user, UserSignIn
from database.connection import get_db
from database.model import User
user_router = APIRouter()

@user_router.post("/signup")
async def sign_new_user(user: Signup_user, db=Depends(get_db)):
    if user.email in user:
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail="이미 등록된 이메일이 있습니다."
        )
    db_user = dict(user)
    users = User(**db_user)
    db.add(users)
    db.commit()
    return {
        "message": "회원가입에 성공했습니다."
    }

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn, db=Depends(get_db)):
    print(user.password, "user.password")
    if user.email not in db or db[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="이메일 또는 비밀번호를 다시 확인해주세요."
        )
    return {
        "message": "로그인 성공했습니다."
    }