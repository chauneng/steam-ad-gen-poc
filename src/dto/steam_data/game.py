"""Game Data Transfer Object"""

from typing import Optional

from pydantic import BaseModel, Field

from src.dto.steam_reviews_response.query_summary import QuerySummary


class GameDTO(BaseModel):
    """Data Transfer Object for a game."""

    id: int = Field(..., description="Steam app ID")
    recent_cursor: Optional[str] = Field(
        None, description="Cursor for continuous fetching"
    )
    query_summary: Optional[QuerySummary] = Field(
        None, description="Summary of reviews for the game"
    )
