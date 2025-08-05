"""Data Transfer Object for creating or updating a game."""
from pydantic import BaseModel, Field


class UpsertGameDTO(BaseModel):
    """Data Transfer Object for creating or updating a game."""
    id: int = Field(..., description="Steam app ID")
