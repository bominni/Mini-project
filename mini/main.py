from fastapi import FastAPI
from database.connection import Base, engine
from routes.users import user_router
from routes.posts import post_router

import uvicorn

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(user_router, prefix="/user")
app.include_router(post_router, prefix="/post")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
