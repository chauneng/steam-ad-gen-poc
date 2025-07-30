"""Game Data Transfer Object"""

from typing import Optional

from pydantic import BaseModel, Field

from src.dto.steam_reviews_response.query_summary import QuerySummary


class GameDTO(BaseModel):
    """Data Transfer Object for a game."""

    id: int = Field(..., description="Steam app ID")
    query_summary: Optional[QuerySummary] = Field(
        None, description="Summary of reviews for the game"
    )
