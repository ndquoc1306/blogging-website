from fastapi import APIRouter

from apis.v1 import route_login

router = APIRouter()

router.include_router(
    route_login.router, prefix="", tags=[""], include_in_schema=False
)
