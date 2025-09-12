from fastapi import APIRouter
from ..schemas.user_schema import UserCreate, UserLogin
from ..crud import user_crud
from ..services import auth_service

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup")
async def signup(user: UserCreate):
    existing_user = await user_crud.get_user_by_username(user.username)
    if existing_user:
        return {"error": "Username already exists"}
    return await user_crud.create_user(user.dict())

@router.post("/login")
async def login(user: UserLogin):
    return await auth_service.authenticate_user(user.username, user.password)