from sqlalchemy import Column, Integer, VARCHAR
from mini.database.connection import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(VARCHAR(20), nullable=False)
    username = Column(VARCHAR(20), nullable=False)
    age = Column(Integer, nullable=False)
    password = Column(VARCHAR(20), nullable=False)