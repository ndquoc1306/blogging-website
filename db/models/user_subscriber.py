from db.base_model import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class UserSubscriber(Base):
    __tablename__ = "USER_SUBSCRIBER"
    __table_args__ = ({'schema': 'C##BLOGWEBSITE'})
    USER_ID = Column(Integer, ForeignKey('C##BLOGWEBSITE.USER.ID'), primary_key=True)
    SUBSCRIBER_ID = Column(Integer, ForeignKey('C##BLOGWEBSITE.SUBSCRIBERS.SUBSCRIBER_ID'), primary_key=True)
    # user = relationship("USER")