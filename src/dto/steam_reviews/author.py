"""Author information for a Steam review."""

from pydantic import BaseModel


class Author(BaseModel):
    """Author information for a Steam review."""

    steamid: str
    num_games_owned: int
    num_reviews: int
    playtime_forever: int
    playtime_last_two_weeks: int
    playtime_at_review: int
    last_played: int
