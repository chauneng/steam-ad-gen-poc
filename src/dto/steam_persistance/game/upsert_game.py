"""Data Transfer Object for creating or updating a game."""

from typing import Optional
from pydantic import BaseModel, Field


class UpsertGameDTO(BaseModel):
    """Data Transfer Object for creating or updating a game."""

    id: int = Field(..., description="Steam app ID")
    recent_cursor: Optional[str] = Field(
        None, description="Cursor for continuous fetching"
    )
