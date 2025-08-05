"""Tied to the upsert response for a game in the Steam persistence layer."""

from pydantic import BaseModel, Field

from .game.upsert_game import UpsertGameDTO
from .review.upsert_query_summary import UpsertReviewQuerySummaryDTO
from .review.upsert_review import UpsertReviewDTO
from .user.upsert_user import UpsertUserDTO
from .user.upsert_user_game_stat import UpsertUserGameStatsDTO


class UpsertResponseDTO(BaseModel):
    """Data Transfer Object for upsert stream review responses."""

    game: UpsertGameDTO = Field(..., description="Game data")
    users: list[UpsertUserDTO] = Field(..., description="List of user data")
    user_stats: list[UpsertUserGameStatsDTO] = Field(
        ..., description="List of user statistics data"
    )
    reviews: list[UpsertReviewDTO] = Field(..., description="List of review data")
    query_summary: UpsertReviewQuerySummaryDTO = Field(
        ..., description="Review query summary data"
    )
