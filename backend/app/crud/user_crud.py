from ..database import db
from ..utils.security import hash_password

async def create_user(user_data: dict):
    user_data["password"] = hash_password(user_data["password"])
    result = await db.users.insert_one(user_data)
    user = await db.users.find_one({"_id": result.inserted_id})
    user["id"] = str(user["_id"])
    return user

async def get_user_by_username(username: str):
    user = await db.users.find_one({"username": username})
    if user:
        user["id"] = str(user["_id"])
    return user
    