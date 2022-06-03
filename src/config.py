from fastapi import FastAPI
import logging
import sys

app = FastAPI()


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
