from typing import Optional
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from pydantic.fields import Field


class Feedback(BaseModel):
    player_name: str
    vote: int
    prediction: str
    confidence: float = Field(default=0, ge=0, le=1)
    subject_id: int
    feedback_text: Optional[str] = None
    proposed_label: Optional[str] = None


router = APIRouter()

@router.get("/v1/feedback/count", tags=["Feedback"])
async def get_feedback(name: str):
    raise HTTPException(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        detail="The Plugin is currently in Safe Mode while we restore full functionality.",
    )

@router.post("/v1/feedback/", status_code=status.HTTP_201_CREATED, tags=["Feedback"])
async def post_feedback(feedback: Feedback):
    raise HTTPException(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        detail="The Plugin is currently in Safe Mode while we restore full functionality.",
    )