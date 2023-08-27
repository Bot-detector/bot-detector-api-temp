import logging
import sys
from typing import List, Optional

import aiohttp
from fastapi import status
from fastapi.exceptions import HTTPException

import src
from src.cogs import classifier, predict, train_model
from src.cogs.highscore_api import HighscoreApi
from src.cogs.Inputs import Inputs
from src.cogs.validation.player import Player
from src.config import app
from src.routers import feedback, legacy, report

sys.modules["api"] = src
sys.modules["api.MachineLearning.classifier"] = src.cogs.classifier

highscore_stat = Inputs.skills + Inputs.minigames + Inputs.bosses
logger = logging.getLogger(__name__)

binary_classifier = classifier.classifier("binaryClassifier").load()
multi_classifier = classifier.classifier("multiClassifier").load()

if binary_classifier is None or multi_classifier is None:
    binary_classifier = classifier.classifier("binaryClassifier")
    multi_classifier = classifier.classifier("multiClassifier")

app.include_router(feedback.router)
app.include_router(legacy.router)
app.include_router(report.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/favicon")
async def favicon():
    return {}


@app.get("/train")
def train():
    if 1:
        raise HTTPException(
            status_code=status.HTTP_418_IM_A_TEAPOT,
            detail="The Plugin is currently in Safe Mode while we restore full functionality.",
        )
    global binary_classifier, multi_classifier
    train_model.train(binary_classifier, multi_classifier)
    binary_classifier = classifier.classifier("binaryClassifier").load()
    multi_classifier = classifier.classifier("multiClassifier").load()
    return {"detail": "model trained"}


####################
@app.get("/v1/prediction", tags=["Prediction"])
async def get_account_prediction_result(name: str, breakdown: Optional[bool] = False):
    # scrape hiscores
    player = {"id": 1, "name": name}
    highscore_api = HighscoreApi(proxy="")
    async with aiohttp.ClientSession() as session:
        player_data = await highscore_api.lookup_hiscores(
            player=Player(id=1, name=name), session=session
        )
        # logger.debug(player_data)

    if player_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The Player is not found on the hiscores.",
        )

    player_data["Tempoross"] = player_data.pop("tempoross")
    # _ = [print({k: v}) for k, v in player_data.items()]
    # _ = player_data.pop("PvP Arena - Rank")
    # _ = player_data.pop("rifts_closed")

    data = predict.predict([player_data], [player], binary_classifier, multi_classifier)
    data = data[0]
    # [logger.debug({k:v}) for k,v in data.items()]
    data = {
        "player_id": data.pop("id"),
        "player_name": data.pop("name"),
        "prediction_label": data.pop("Prediction"),
        "prediction_confidence": float(data.pop("Predicted_confidence")) / 100,
        "created": data.pop("created"),
        "predictions_breakdown": {k: float(v) / 100 for k, v in data.items()},
    }
    return data
