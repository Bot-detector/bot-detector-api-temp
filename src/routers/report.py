from pydantic import BaseModel
from pydantic.fields import Field
from fastapi import APIRouter, HTTPException, Query, Request, status

upper_gear_cost = 1_000_000_000_000

class equipment(BaseModel):
    equip_head_id: int = Field(None, ge=0)
    equip_amulet_id: int = Field(None, ge=0)
    equip_torso_id: int = Field(None, ge=0)
    equip_legs_id: int = Field(None, ge=0)
    equip_boots_id: int = Field(None, ge=0)
    equip_cape_id: int = Field(None, ge=0)
    equip_hands_id: int = Field(None, ge=0)
    equip_weapon_id: int = Field(None, ge=0)
    equip_shield_id: int = Field(None, ge=0)


class detection(BaseModel):
    reporter: str = Field(..., min_length=1, max_length=13)
    reported: str = Field(..., min_length=1, max_length=12)
    region_id: int = Field(0, ge=0, le=100_000)
    x_coord: int = Field(0, ge=0)
    y_coord: int = Field(0, ge=0)
    z_coord: int = Field(0, ge=0)
    ts: int = Field(0, ge=0)
    manual_detect: int = Field(0, ge=0, le=1)
    on_members_world: int = Field(0, ge=0, le=1)
    on_pvp_world: int = Field(0, ge=0, le=1)
    world_number: int = Field(0, ge=300, le=1_000)
    equipment: equipment
    equip_ge_value: int = Field(0, ge=0, le=int(upper_gear_cost))



router = APIRouter()

@router.post("/v1/report", status_code=status.HTTP_201_CREATED, tags=["Report"])
async def insert_report(
    detections: list[detection],
    manual_detect: int = Query(None, ge=0, le=1),
):
    raise HTTPException(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        detail="The Plugin is currently in Safe Mode while we restore full functionality.",
    )

@router.get("/v1/report/count", tags=["Report"])
@router.get("/v1/report/manual/count", tags=["Report"])
async def get_report_count_v1(name: str):
    raise HTTPException(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        detail="The Plugin is currently in Safe Mode while we restore full functionality.",
    )
