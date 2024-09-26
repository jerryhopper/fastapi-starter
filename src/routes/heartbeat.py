from fastapi import APIRouter

from typing import Annotated, Union
from fastapi import  HTTPException, status, Header, Depends


heartbeat_router = APIRouter()


@heartbeat_router.get("/heartbeat")
async def root():
    return {"message": "Hello World"}



# https://fastapi.tiangolo.com/tutorial/header-params/
@heartbeat_router.get("/headers")
async def read_headers(user_agent: Annotated[Union[str, None], Header()] = None,accept: Annotated[Union[str, None], Header()] = None):
    return {"User-Agent": user_agent,"Accept": accept}


