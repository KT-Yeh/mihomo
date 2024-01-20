from pydantic import BaseModel

from .character import Character
from .player import Player


class StarrailInfoParsed(BaseModel):
    """
    Mihomo parsed data

    Attributes:
        - player (`Player`): The player's info.
        - characters (list[`Character`]): The list of characters.
    """

    player: Player
    """Player's basic info"""
    characters: list[Character]
    """The list of characters"""
