from fastapi import HTTPException, status
from ..crud import user_crud
from ..utils.security import verify_password, create_access_token

async def authenticate_user(username: str, password: str):
    user = await user_crud.get_user_by_username(username)
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token({"sub": user["username"], "id": str(user["id"])})
    return {"access_token": token, "token_type": "bearer"}