"""Data Transfer Object for creating or updating a review query summary."""

from typing import Optional

from pydantic import BaseModel, Field


class UpsertReviewQuerySummaryDTO(BaseModel):
    """Data Transfer Object for creating or updating a review query summary."""
    id: Optional[int] = Field(
        None, description="Review Query Summary ID"
    )
    game_id: int = Field(..., description="Game ID")
    num_reviews: Optional[int] = Field(
        None, description="Total number of reviews"
    )
    review_score: Optional[float] = Field(
        None, description="Overall review score"
    )
    review_score_desc: Optional[str] = Field(
        None, description="Description of the review score"
    )
    total_positive: Optional[int] = Field(
        None, description="Number of positive reviews"
    )
    total_negative: Optional[int] = Field(
        None, description="Number of negative reviews"
    )
    total_reviews: Optional[int] = Field(
        None, description="Total number of reviews"
    )
    cursor: Optional[str] = Field(
        None, description="Cursor for pagination"
    )
