from fastapi import status
from fastapi.exceptions import HTTPException

from src.config import app


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/favicon")
async def favicon():
    return {}


@app.post("/{version}/plugin/detect/{manual_detect}")
async def post_detect(version, manual_detect):
    raise HTTPException(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        detail="We are currently having database issues, our admins are on it!",
    )


@app.get("/{version}/stats/contributions/{contributor}")
async def get_contributions(version, contributor):
    raise HTTPException(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        detail="We are currently having database issues, our admins are on it!",
    )


@app.get("/{version}/site/prediction/{player_name}")
async def get_prediction(player_name, version=None, token=None):
    # TODO: scrape hiscores
    # TODO: parse data
    # TODO: post to ML
    # TODO: return prediction
    raise HTTPException(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        detail="We are currently having database issues, our admins are on it!",
    )
