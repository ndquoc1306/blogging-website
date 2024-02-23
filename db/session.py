# create_engine
# session_maker
# Generator -> typing
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator
from sqlalchemy.engine.url import URL

# SQLite connection
# connect_url = "sqlite:///./sql_app.db"

# Oracle Connection

username = "sys"
password = "123456"
host = "localhost"
port = "1251"
sid = "ORCLCDB"
engine = create_engine(f"oracle+cx_oracle://{username}:{password}@(DESCRIPTION = (LOAD_BALANCE=on) (FAILOVER=ON) (ADDRESS = (PROTOCOL = TCP)(HOST = {host})(PORT = 1521)) (CONNECT_DATA = (SERVER = DEDICATED) (SID = {sid})))?encoding=UTF-8&nencoding=UTF-8&mode=SYSDBA&events=true")

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
