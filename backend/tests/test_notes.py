import pytest
from httpx import AsyncClient
from app.main import app
from app.utils.security import create_access_token

@pytest.mark.asyncio
async def test_create_read_update_delete_note():
    token = create_access_token({"sub": "testuser", "id": "123"})
    headers = {"Authorization": f"Bearer {token}"}

    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create note
        response = await ac.post("/notes/", json={"title": "Note1", "content": "Markdown content"}, headers=headers)
        assert response.status_code == 200
        note = response.json()
        note_id = note["id"]

        # Read notes
        response = await ac.get("/notes/", headers=headers)
        assert response.status_code == 200
        notes = response.json()
        assert len(notes) > 0

        # Update note
        response = await ac.put(f"/notes/{note_id}", json={"title": "Updated", "content": "Updated content"}, headers=headers)
        assert response.status_code == 200
        updated_note = response.json()
        assert updated_note["title"] == "Updated"

        # Delete note
        response = await ac.delete(f"/notes/{note_id}", headers=headers)
        assert response.status_code == 200