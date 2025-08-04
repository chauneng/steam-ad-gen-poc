"""model for storing Steam review responses query summaries."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.models.base_model import BaseModel, CommonMixin, TimestampMixin


class ReviewQuerySummary(CommonMixin, TimestampMixin, BaseModel):
    """Model for storing Steam review responses query summaries."""

    id = Column(Integer, primary_key=True, autoincrement=True)
    game_id = Column(Integer, ForeignKey("game.id"), nullable=False)
    num_reviews = Column(Integer, nullable=False)
    review_score = Column(Integer, nullable=False)
    review_score_desc = Column(String, nullable=False)
    total_positive = Column(Integer, nullable=False)
    total_negative = Column(Integer, nullable=False)
    total_reviews = Column(Integer, nullable=False)
    cursor = Column(String, nullable=True)

    game = relationship(
        "Game",
        back_populates="review_query_summaries",
        cascade="save-update, merge",
    )
