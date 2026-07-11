from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.services.chat_service import generate_chat_response

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


class ChatRequest(BaseModel):
    message: str = Field(min_length=1)
    cv_skills: list[str] = []
    job: dict[str, Any] | None = None


@router.post("/")
def chat(data: ChatRequest):
    response = generate_chat_response(
        message=data.message,
        cv_skills=data.cv_skills,
        job=data.job
    )

    return {
        "success": True,
        "response": response
    }