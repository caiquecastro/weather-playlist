from pydantic import BaseModel
from typing import List

class PlaylistSong(BaseModel):
    name: str


class CityPlaylist(BaseModel):
    city: str
    temperature: float
    playlist: List[PlaylistSong]


class CityStats(BaseModel):
    city: str
    visits: int


class Error(BaseModel):
    detail: str
