from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from db.base_model import Base


class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    content = Column(Text, nullable=True)

    author_id = Column(Integer, ForeignKey("user.id"))
    author = relationship("User", back_populates="blogs")

    created_at = Column(DateTime, default=datetime.now())
    is_acvite = Column(Boolean, default=True)
