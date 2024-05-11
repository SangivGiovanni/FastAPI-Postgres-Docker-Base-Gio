from sqlalchemy import Column, Integer, String, Text
from db.database import Base


class Blogs(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    url = Column(String)
