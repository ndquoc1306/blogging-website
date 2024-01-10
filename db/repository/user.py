from sqlalchemy.orm import Session

from res_models.user import CreateUser
from db.models.user import User
from core.hashing import Hasher


def create_new_user(user: CreateUser, db: Session):
    user = User(
        email=user.email,
        password=Hasher.get_hashed_password(user.password),
        is_superadmin=False,
        is_active=True,
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()
