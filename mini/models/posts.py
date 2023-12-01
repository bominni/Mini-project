from pydantic import BaseModel
from typing import List

class Post(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "content": "We will be discussing the contensts of the FastAPI book in this event."
            }
        }