import pandas as pd
from src.cogs import data
from src.cogs.classifier import classifier
from sklearn.model_selection import train_test_split
import logging

logger = logging.getLogger(__name__)

def train(binary_classifier:classifier, multi_classifier:classifier):
    logger.debug("reading hiscores")
    hiscores = pd.read_csv("src/cogs/data/hiscores.csv").to_dict(orient="records")
    logger.debug("reading players")
    players = pd.read_csv("src/cogs/data/players.csv").to_dict(orient="records")
    logger.debug("reading labels")
    labels = pd.read_csv("src/cogs/data/labels.csv").to_dict(orient="records")

    logger.debug("creating hiscoredata")
    hiscoredata = data.hiscoreData(hiscores)

    logger.debug("creating features")
    features = hiscoredata.features()
    
    logger.debug("creating playerdata")
    player_data = data.playerData(players, labels).get(binary=True)

    logger.debug("merge features with players")
    features_labeled = features.merge(player_data, left_index=True, right_index=True)

    # create train test data
    x, y = features_labeled.iloc[:, :-1], features_labeled.iloc[:, -1]
    train_x, test_x, train_y, test_y = train_test_split(
        x, y, test_size=0.2, random_state=42, stratify=y
    )

    # train & score the model
    binary_classifier.fit(train_x, train_y)
    binary_classifier.score(test_y, test_x)

    # save the model
    binary_classifier.save()

    # get players with multi target
    player_data = data.playerData(players, labels).get(binary=False)

    # merge features with target
    features_labeled = features.merge(player_data, left_index=True, right_index=True)

    # we need at least 100 users
    to_little_data_labels = (
        pd.DataFrame(features_labeled.iloc[:, -1].value_counts())
        .query("target < 100")
        .index
    )
    mask = ~(features_labeled["target"].isin(to_little_data_labels))
    features_labeled = features_labeled[mask]

    # create train test data
    x, y = features_labeled.iloc[:, :-1], features_labeled.iloc[:, -1]
    train_x, test_x, train_y, test_y = train_test_split(
        x, y, test_size=0.2, random_state=42, stratify=y
    )

    # train & score the model
    multi_classifier.fit(train_x, train_y)
    multi_classifier.score(test_y, test_x)

    # save the model
    multi_classifier.save()
    return {"detail": "ok"}