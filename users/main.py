"""
Simple user management microservice for testing microservice communication patterns.

Provides basic CRUD operations for users with in-memory storage.
No external dependencies or complex patterns - designed for experimentation.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="User Service")


# Simple in-memory storage
users = []


class UserCreate(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str


@app.get("/")
async def root() -> dict[str, str]:
    return {"service": "User Service", "status": "running"}


@app.get("/users", response_model=list[UserResponse])
async def get_users() -> list[UserResponse]:
    return [
        UserResponse(**user)
        for user in users
    ]


@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int) -> UserResponse:
    for user in users:
        if user["id"] == user_id:
            return UserResponse(**user)
    
    raise HTTPException(status_code=404, detail="User not found.")


@app.post("/users", response_model=UserCreate)
async def create_user(user: UserResponse) -> UserResponse:
    id = len(users) + 1
    
    user_data = {
        "id": id,
        "name": user.name,
        "email": user.email
    }

    users.append(user_data)

    return UserResponse(**user_data)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "healthy", "service": "user-service"}
