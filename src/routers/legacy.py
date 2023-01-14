from fastapi import APIRouter, HTTPException, status, Request
from pydantic import BaseModel

router = APIRouter()

class discord(BaseModel):
    player_name: str
    code: str

@router.post("/{version}/site/discord_user/{token}", tags=["Legacy"])
async def verify_discord_user(
    token: str, discord: discord, request: Request, version: str = None
):
    raise HTTPException(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        detail="The Plugin is currently in Safe Mode while we restore full functionality.",
    )