"""
Simple notification management microservice for testing microservice communication patterns.

Handles notification creation and retrieval with in-memory storage.
Designed as a companion service for microservice communication experiments.
"""
import time

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Notification Service")


# Simple in-memory storage
notifications = []


class NotificationCreate(BaseModel):
    user_id: int
    message: str
    email: str
    timestamp: float


class NotificationResponse(BaseModel):
    id: int
    user_id: int
    message: str
    email: str
    timestamp: float


@app.get("/")
async def root() -> dict[str, str]:
    return {"service": "Notification Service", "status": "running"}


@app.get("/notifications", response_model=list[NotificationResponse])
async def get_notifications() -> list[NotificationResponse]:
    return [
        NotificationResponse(**notification)
        for notification in notifications
    ]


@app.get("/notifications/{notification_id}", response_model=NotificationResponse)
async def get_notification(notification_id: int) -> NotificationResponse:
    for notification in notifications:
        if notification["id"] == notification_id:
            return NotificationResponse(**notification)
    
    raise HTTPException(status_code=404, detail="Notification not found.")


@app.post("/notifications", response_model=NotificationCreate)
async def create_notification(notification: NotificationResponse) -> NotificationResponse:
    id = len(notifications) + 1

    notification_data = {
        "id": id,
        "user_id": notification.user_id,
        "message": notification.message,
        "email": notification.email,
        "timestamp": time.time()
    }

    notifications.append(notification_data)

    return NotificationResponse(**notification_data)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "healthy", "service": "notification-service"}
