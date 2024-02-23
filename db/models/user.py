from db.base_model import Base
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship

from db.models.user_subscriber import UserSubscriber


class User(Base):
    __tablename__ = "USER"
    __table_args__ = ({'schema': 'C##BLOGWEBSITE'})
    ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    EMAIL = Column(String, nullable=False, unique=True, index=True)
    PASSWORD = Column(String, nullable=False)
    IS_SUPERADMIN = Column(Boolean, default=False)
    IS_ACTIVE = Column(Boolean, default=True)
    # blogs = relationship("Blog", back_populates="author")
    # subscribers = relationship("User", secondary=UserSubscriber, back_populates="subscribers")

