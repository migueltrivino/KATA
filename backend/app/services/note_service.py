from bson import ObjectId
from app.database import db  


async def get_notes_by_user(user_id: str):
    notes = await db.notes.find({"owner_id": user_id}).to_list(100)
    for note in notes:
        note["_id"] = str(note["_id"])  
    return notes


async def create_note(title: str, content: str, owner_id: str):
    note = {
        "title": title,
        "content": content,
        "owner_id": owner_id
    }
    result = await db.notes.insert_one(note)
    note["_id"] = str(result.inserted_id)
    return note


async def update_note(note_id: str, owner_id: str, title: str, content: str):
    result = await db.notes.update_one(
        {"_id": ObjectId(note_id), "owner_id": owner_id},
        {"$set": {"title": title, "content": content}}
    )
    if result.modified_count:
        return await db.notes.find_one({"_id": ObjectId(note_id)})
    return None


async def delete_note(note_id: str, owner_id: str):
    result = await db.notes.delete_one({"_id": ObjectId(note_id), "owner_id": owner_id})
    return result.deleted_count