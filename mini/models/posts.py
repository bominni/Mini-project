from pydantic import BaseModel
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