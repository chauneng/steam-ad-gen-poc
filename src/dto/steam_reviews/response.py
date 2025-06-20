"""Response DTO for Steam Reviews API."""

from typing import List

from pydantic import BaseModel

from .query_summary import QuerySummary
from .review import Review


class SteamReviewsResponse(BaseModel):
    """Response DTO for Steam Reviews API."""

    success: int
    query_summary: QuerySummary
    reviews: List[Review]
    cursor: str
