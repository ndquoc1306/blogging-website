# create_engine
# session_maker
# Generator -> typing
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator
from sqlalchemy.engine.url import URL

connect_url = "sqlite:///./sql_app.db"
# connect_url = "oracle+cx_oracle://quoc:quoc@localhost:1521/QUOC"

# connect_url = URL(
#     "oracle+cx_oracle",
#     username="quoc",
#     password="quoc",
#     host="localhost",
#     port="1251",
#     database="QUOC"
# )


engine = create_engine(connect_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

####################################################################
# from sqlalchemy.orm import declarative_base

# Base = declarative_base()
