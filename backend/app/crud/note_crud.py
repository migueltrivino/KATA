from ..database import db
from bson import ObjectId

async def create_note(note_data: dict):
    result = await db.notes.insert_one(note_data)
    note = await db.notes.find_one({"_id": result.inserted_id})
    note["id"] = str(note["_id"])  
    return note

async def get_notes(owner_id: str):
    notes_cursor = db.notes.find({"owner_id": ObjectId(owner_id)})
    notes = []
    async for note in notes_cursor:
        note["id"] = str(note["_id"])
        notes.append(note)
    return notes

async def get_note(note_id: str, owner_id: str):
    note = await db.notes.find_one({
        "_id": ObjectId(note_id),
        "owner_id": ObjectId(owner_id)
    })
    if note:
        note["id"] = str(note["_id"])
    return note

async def update_note(note_id: str, owner_id: str, content: str):
    result = await db.notes.update_one(
        {"_id": ObjectId(note_id), "owner_id": ObjectId(owner_id)},
        {"$set": {"content": content}}
    )
    if result.modified_count:
        return await get_note(note_id, owner_id)
    return None

async def delete_note(note_id: str, owner_id: str):
    result = await db.notes.delete_one({
        "_id": ObjectId(note_id),
        "owner_id": ObjectId(owner_id)
    })
    return result.deleted_count