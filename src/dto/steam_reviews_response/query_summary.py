"""Summary of the query results for Steam API."""

from typing import Optional

from pydantic import BaseModel


class QuerySummary(BaseModel):
    """Summary of the query results for Steam API."""

    num_reviews: int
    review_score: Optional[int] = None
    review_score_desc: Optional[str] = None
    total_positive: Optional[int] = None
    total_negative: Optional[int] = None
    total_reviews: Optional[int] = None
