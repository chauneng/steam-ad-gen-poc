"""Summary of the query results for Steam API."""

from pydantic import BaseModel


class QuerySummary(BaseModel):
    """Summary of the query results for Steam API."""
    num_reviews: int
    review_score: int
    review_score_desc: str
    total_positive: int
    total_negative: int
    total_reviews: int
