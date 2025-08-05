"""Steam reviews author information."""

from pydantic import BaseModel


class Author(BaseModel):
    """
    Detailed information about the author of a Steam review.
    playtimes are in minutes.
    last_played is a Unix timestamp.
    """

    steamid: int
    num_games_owned: int
    num_reviews: int
    playtime_forever: int
    playtime_last_two_weeks: int
    playtime_at_review: int
    last_played: int
