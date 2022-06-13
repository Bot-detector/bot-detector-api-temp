import imp
import logging

import aiohttp
from fastapi import status
from fastapi.exceptions import HTTPException

from src.cogs.scraper import Scraper
from src.config import app
from src.cogs import predict
from src.cogs import classifier
from src.cogs import train_model


logger = logging.getLogger(__name__)

scraper = Scraper(proxy="")

binary_classifier = classifier.classifier("binaryClassifier").load()
multi_classifier = classifier.classifier("multiClassifier").load()

if binary_classifier is None or multi_classifier is None:
    binary_classifier = classifier.classifier("binaryClassifier")
    multi_classifier = classifier.classifier("multiClassifier")

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
    return {
        "detail": "model trained"
    }

@app.post("/{version}/plugin/detect/{manual_detect}")
async def post_detect(version, manual_detect):
    raise HTTPException(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        detail="The Plugin is currently in Safe Mode while we restore full functionality.",
    )


@app.get("/{version}/stats/contributions/{contributor}")
async def get_contributions(version, contributor):
    raise HTTPException(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        detail="The Plugin is currently in Safe Mode while we restore full functionality.",
    )


@app.get("/{version}/site/prediction/{player_name}")
async def get_prediction(player_name, version=None, token=None):
    # scrape hiscores
    player = {"id": 1, "name": player_name}
    async with aiohttp.ClientSession() as session:
        player_data = await scraper.lookup_hiscores(player=player, session=session)

    if player_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The Player is not found on the hiscores.",
        )
        
    data = predict.predict([player_data], [player], binary_classifier, multi_classifier)
    data = data[0]
    # [logger.debug({k:v}) for k,v in data.items()]
    data = {
        "player_id": data.pop("id"),
        "player_name": data.pop("name"),
        "prediction_label": data.pop("Prediction"),
        "prediction_confidence": float(data.pop("Predicted_confidence"))/100,
        "created": data.pop("created"),
        "predictions_breakdown": {k:float(v)/100 for k,v in data.items()},
    }
    return data
