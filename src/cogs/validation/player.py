from pydantic import BaseModel
from typing import Optional

class PlayerDoesNotExistException(Exception):
    pass

class Player(BaseModel):
    id: int
    name: str
    # created_at: str
    # updated_at: str | None
    # possible_ban: int
    # confirmed_ban: int
    # confirmed_player: int
    # label_id: int
    # label_jagex: int