from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db.models.user import User

from db.base_model import Base


class Blog(Base):
    __tablename__ = "BLOG"
    __table_args__ = ({'schema': 'C##BLOGWEBSITE'})
    ID = Column(Integer, primary_key=True, autoincrement=True)
    TITLE = Column(String, nullable=False)
    SLUG = Column(String, nullable=False)
    CONTENT = Column(Text, nullable=True)

    AUTHOR_ID = Column(Integer, ForeignKey(User.ID))
    # author = relationship("User", backref="BLOGS")

    CREATED_AT = Column(DateTime, default=datetime.now())
    IS_ACTIVE = Column(Boolean, default=True)
