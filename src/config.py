from fastapi import FastAPI
import logging
import sys
import numpy as np 

np.random.seed(1337)
app = FastAPI()

LABELS = [
    "Real_Player",
    "PVM_Melee_bot",
    "Smithing_bot",
    "Magic_bot",
    "Fishing_bot",
    "Mining_bot",
    "Crafting_bot",
    "PVM_Ranged_Magic_bot",
    "Hunter_bot",
    "Fletching_bot",
    "LMS_bot",
    "Agility_bot",
    "Wintertodt_bot",
    "Runecrafting_bot",
    "Zalcano_bot",
    "Woodcutting_bot",
    "Thieving_bot",
    "Soul_Wars_bot",
    "Cooking_bot",
    "Vorkath_bot",
    "Barrows_bot",
    "Herblore_bot",
    "Zulrah_bot",
    "Unknown_bot"
]


# setup logging
file_handler = logging.FileHandler(filename="error.log", mode="a")
stream_handler = logging.StreamHandler(sys.stdout)

# log formatting
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

handlers = [file_handler, stream_handler]

logging.basicConfig(level=logging.DEBUG, handlers=handlers)

logging.getLogger("urllib3").setLevel(logging.INFO)
