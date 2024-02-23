from db.base_model import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from db.models.user_subscriber import UserSubscriber


class Subscribers(Base):
    __tablename__ = "SUBSCRIBERS"
    __table_args__ = ({'schema': 'C##BLOGWEBSITE'})
    SUBSCRIBER_ID = Column(Integer, primary_key=True, autoincrement=True)
    EMAIL = Column(String, unique=True, nullable=False)
    # subscribers = relationship("Subscriber", secondary=UserSubscriber, back_populates="users")

