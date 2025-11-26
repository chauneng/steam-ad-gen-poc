"""Result from querying Steam for review summary data."""

from pydantic import BaseModel, Field


class ReviewQuerySummaryDTO(BaseModel):
    """Result from querying Steam for review summary data."""
    model_config = {"from_attributes": True}

    id: int = Field(..., description="Review Query Summary ID")
    game_id: int = Field(..., description="Steam App ID of the game")
    num_reviews: int = Field(..., description="Number of reviews in the query result")
    review_score: int = Field(..., description="Overall review score")
    review_score_desc: str = Field(..., description="Description of the review score")
    total_positive: int = Field(..., description="Total number of positive reviews")
    total_negative: int = Field(..., description="Total number of negative reviews")
    total_reviews: int = Field(..., description="Total number of reviews for the game")
    cursor: str = Field(..., description="Cursor for pagination")
