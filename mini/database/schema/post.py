from sqlalchemy import Column, Integer, VARCHAR, Text, ForeignKey
from mini.database.connection import Base
from sqlalchemy.orm import relationship
class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    title = Column(VARCHAR(255), nullable=False)
    content = Column(Text, nullable=False)
    user = relationship("User", backref="post")