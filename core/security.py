from typing import Optional
from datetime import timedelta, datetime, timezone
from jose import jwt

from core.config import setting


def create_access_token(data: dict, expire_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expire_delta:
        expire = datetime.now() + expire_delta
    else:
        expire = datetime.now() + timedelta(minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES)

    expire = expire.astimezone(timezone.utc)

    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, key=setting.SECRET_KEY, algorithm=setting.ALGORITHM)