from sqlalchemy import Column, Integer, VARCHAR, Text, ForeignKey
from sqlalchemy.orm import relationship
from .connection import Base
class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    title = Column(VARCHAR(255), nullable=False)
    content = Column(Text, nullable=False)
    user = relationship("User", backref="post")

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(VARCHAR(20), nullable=False)
    username = Column(VARCHAR(20), nullable=False)
    age = Column(Integer, nullable=False)
    password = Column(VARCHAR(20), nullable=False)