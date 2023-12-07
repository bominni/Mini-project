from fastapi import APIRouter, Body, HTTPException, status
from models.posts import Post
from typing import List

post_router = APIRouter()

posts = []

@post_router.get("/list", response_model=List[Post])
async def retrieve_post() -> List[Post]:
    return posts

@post_router.post("/create")
async def create_post(body: Post = Body(...)) -> dict:
    posts.append(dict(body))
    return {
        "message": "게시물이 생성되었습니다."
    }

@post_router.patch("/change")
async def change_post(body: Post = Body(...)) -> dict:
    for post in posts:
        if body["id"] == post["id"]:
            post["title"] = body["title"]
            post["content"] = body["content"]
            return {
                "message" : "수정되었습니다."
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="해당 게시판은 없는 게시판입니다. 다시 한번 확인해주세요."
    )

@post_router.delete("/delete/{id}")
async def delete_post(id: int) -> dict:
    for post in posts:
        if id == post["id"]:
            posts.remove(post)
            return {
                "message": "해당 글이 삭제되었습니다."
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="해당 게시판은 없는 게시판입니다. 다시 한번 확인해주세요."
    )