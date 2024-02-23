from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status, Request
from jose import jwt, JWTError
from fastapi.security.utils import get_authorization_scheme_param

from db.repository.user import get_user
from core.security import create_access_token
from core.hashing import Hasher
from res_models.token import Token
from db.session import get_db
from core.config import setting

router = APIRouter()


def authenticate_user(email: str, password: str, db: Session):
    user = get_user(email=email, db=db)
    if not user:
        return False
    if not Hasher.verify_password(password, user.PASSWORD):
        return False
    return user


@router.post("/token", response_model=Token)
def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(
        email=form_data.username, password=form_data.password, db=db
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect Username or Password",
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def get_current_user(
        token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credetials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect Username or Password",
    )

    try:
        payload = jwt.decode(
            token=token, key=setting.SECRET_KEY, algorithms=[setting.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credetials_exception


    except JWTError:
        raise credetials_exception
    user = get_user(email=username, db=db)
    if user is None:
        raise credetials_exception
    return user


@router.get("/test")
def test(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    _, token = get_authorization_scheme_param(token)
    try:
        user = get_current_user(token=token, db=db)
    except Exception:
        return {"error": "error"}
    return user
