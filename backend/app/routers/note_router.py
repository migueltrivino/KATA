from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..schemas.note_schema import NoteCreate, NoteUpdate, NoteOut
from ..crud import note_crud
from fastapi.security import OAuth2PasswordBearer
from ..utils import security
from bson import ObjectId

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = security.decode_access_token(token)
        return {"username": payload["sub"], "id": payload["id"]}
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

router = APIRouter(prefix="/notes", tags=["notes"])

def serialize_note(note: dict) -> dict:
    
    note["_id"] = str(note["_id"])
    note["owner_id"] = str(note["owner_id"])
    return note

@router.post("/", response_model=NoteOut)
async def create_note(note: NoteCreate, user=Depends(get_current_user)):
    if not note.content.strip():
        raise HTTPException(status_code=400, detail="Content cannot be empty")
    data = note.dict()
    data["owner_id"] = ObjectId(user["id"])
    created_note = await note_crud.create_note(data)
    return serialize_note(created_note)

@router.get("/", response_model=List[NoteOut])
async def read_notes(user=Depends(get_current_user)):
    notes = await note_crud.get_notes(ObjectId(user["id"]))
    return [serialize_note(n) for n in notes]

@router.put("/{note_id}", response_model=NoteOut)
async def update_note(note_id: str, note: NoteUpdate, user=Depends(get_current_user)):
    if not note.content.strip():
        raise HTTPException(status_code=400, detail="Content cannot be empty")
    updated = await note_crud.update_note(
        ObjectId(note_id),
        ObjectId(user["id"]),
        note.content
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Note not found")
    return serialize_note(updated)

@router.delete("/{note_id}")
async def delete_note(note_id: str, user=Depends(get_current_user)):
    deleted = await note_crud.delete_note(ObjectId(note_id), ObjectId(user["id"]))
    if not deleted:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"detail": "Note deleted"}