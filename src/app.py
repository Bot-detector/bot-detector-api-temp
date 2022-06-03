import logging

import aiohttp
from fastapi import status
from fastapi.exceptions import HTTPException

from src.cogs.scraper import Scraper
from src.config import app

logger = logging.getLogger(__name__)

scraper = Scraper(proxy="")


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
    # scrape hiscores
    player = {"id": 1, "name": player_name}
    async with aiohttp.ClientSession() as session:
        player_data = await scraper.lookup_hiscores(player=player, session=session)
    logger.debug(player_data)
    # TODO: parse data
    # TODO: post to ML
    # TODO: return prediction
    raise HTTPException(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        detail="We are currently having database issues, our admins are on it!",
    )
