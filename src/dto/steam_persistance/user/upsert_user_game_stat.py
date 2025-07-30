"""Data Transfer Object for creating or updating a user's game stats."""

from typing import Optional

from pydantic import BaseModel, Field


class UpsertUserGameStatsDTO(BaseModel):
    """Data Transfer Object for creating or updating a user's game stats."""

    user_id: int = Field(..., description="User ID")
    game_id: int = Field(..., description="Game ID")
    playtime_forever: Optional[int] = Field(
        None, description="Total playtime of the game by the user"
    )
    playtime_last_two_weeks: Optional[int] = Field(
        None, description="Playtime of the game in the last two weeks by the user"
    )
    playtime_at_review: Optional[int] = Field(
        None, description="Playtime of the game at the time of review by the user"
    )
    last_played: Optional[int] = Field(
        None, description="Last played date of the game by the user"
    )
