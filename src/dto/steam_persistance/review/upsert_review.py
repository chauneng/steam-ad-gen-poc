"""Data Transfer Object for creating or updating a user's review."""

from typing import Optional

from pydantic import BaseModel, Field


class UpsertReviewDTO(BaseModel):
    """Data Transfer Object for creating or updating a user's review."""
    id: int = Field(..., description="Review ID")
    user_id: int = Field(..., description="User ID")
    game_id: int = Field(..., description="Game ID")
    language: Optional[str] = Field(None, description="Language of the review")
    review_text: Optional[str] = Field(None, description="Text of the review")
    created_at: Optional[int] = Field(
        None, description="Timestamp when the review was created"
    )
    updated_at: Optional[int] = Field(
        None, description="Timestamp when the review was last updated"
    )
    voted_up: Optional[int] = Field(
        None, description="Number of upvotes for the review"
    )
    votes_up: Optional[int] = Field(
        None, description="Number of upvotes for the review"
    )
    votes_funny: Optional[int] = Field(
        None, description="Number of funny votes for the review"
    )
    weighted_vote_score: Optional[float] = Field(
        None, description="Weighted score of the review based on votes"
    )
    comment_count: Optional[int] = Field(
        None, description="Number of comments on the review"
    )
    steam_purchase: Optional[bool] = Field(
        None, description="Whether the game was purchased on Steam"
    )
    received_for_free: Optional[bool] = Field(
        None, description="Whether the game was received for free"
    )
    written_during_early_access: Optional[bool] = Field(
        None, description="Whether the review was written during early access"
    )
    primarily_steam_deck: Optional[bool] = Field(
        None, description="Whether the review was primarily written for Steam Deck"
    )

