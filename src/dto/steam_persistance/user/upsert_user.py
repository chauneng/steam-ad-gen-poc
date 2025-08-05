"""Data Transfer Object for creating or updating a user."""

from typing import Optional

from pydantic import BaseModel, Field


class UpsertUserDTO(BaseModel):
    """Data Transfer Object for creating or updating a user."""

    id: int = Field(..., description="User ID")
    num_games_owned: Optional[int] = Field(
        None, description="Number of games owned by the user"
    )
    num_reviews: Optional[int] = Field(
        None, description="Number of reviews written by the user"
    )
