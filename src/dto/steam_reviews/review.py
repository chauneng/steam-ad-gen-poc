"""Detailed information about a single review."""

from pydantic import BaseModel

from .author import Author


class Review(BaseModel):
    """Detailed information about a single review."""

    recommendationid: str
    author: Author
    language: str
    review: str
    timestamp_created: int
    timestamp_updated: int
    voted_up: bool
    votes_up: int
    votes_funny: int
    weighted_vote_score: float
    comment_count: int
    steam_purchase: bool
    received_for_free: bool
    written_during_early_access: bool
    primarily_steam_deck: bool
