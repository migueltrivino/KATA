import pytest
from httpx import AsyncClient
from app.main import app
from app.database import db

@pytest.mark.asyncio
async def test_signup_and_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Signup
        response = await ac.post("/auth/signup", json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpass"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["username"] == "testuser"

        # Login
        response = await ac.post("/auth/login", json={
            "username": "testuser",
            "password": "testpass"
        })
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data