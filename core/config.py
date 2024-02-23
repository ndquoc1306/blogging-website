import os
from dotenv import load_dotenv

from pathlib import Path

env_path = Path(".") / ".env"
load_dotenv(env_path)


class Setting:
    APP_TITLE = "Blog App"
    APP_VERSION = "00.00.00"

    SECRET_KEY: str = 'quoc123'
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30


setting = Setting()
