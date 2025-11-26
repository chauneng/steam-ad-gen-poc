"""User Game Statistics Data Transfer Object."""

from datetime import datetime

from pydantic import BaseModel


class UserGameStatDTO(BaseModel):
    """User Game Statistics Data Transfer Object."""

    id: int
    playtime_forever: int
    playtime_last_two_weeks: int
    playtime_at_review: int
    last_played: datetime
    user_id: int
    game_id: int
