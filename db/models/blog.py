from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey,func
from sqlalchemy.orm import relationship

from db.base_class import Base

class Blogs(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    content = Column(Text, nullable=True)
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("Users")
    is_active = Column(Boolean, default=False)

