"""model for storing Steam review responses query summaries."""

from sqlalchemy import BigInteger, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.models.base_model import BaseModel, CommonMixin, TimestampMixin


class ReviewQuerySummary(CommonMixin, TimestampMixin, BaseModel):
    """Model for storing Steam review responses query summaries."""

    id = Column(Integer, primary_key=True, autoincrement=True)
    game_id = Column(BigInteger, ForeignKey("game.id"), nullable=False)
    num_reviews = Column(Integer, nullable=False)
    review_score = Column(Integer, nullable=False)
    review_score_desc = Column(String, nullable=False)
    total_positive = Column(Integer, nullable=False)
    total_negative = Column(Integer, nullable=False)
    total_reviews = Column(Integer, nullable=False)
    cursor = Column(String, nullable=True)

    game = relationship(
        "Game",
        back_populates="review_query_summary",
        cascade="save-update, merge",
    )
