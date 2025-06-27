"""Game model for Steam games."""

from sqlalchemy import BigInteger, Column, Integer, String
from sqlalchemy.orm import relationship

from src.models.base_model import BaseModel, CommonMixin


class Game(CommonMixin, BaseModel):
    """Represents a Steam game with its metadata and reviews."""

    id = Column(Integer, primary_key=True)  # app_id
    num_reviews = Column(Integer, nullable=False)
    review_cursor = Column(String, index=True)
    review_score = Column(Integer, nullable=False)
    review_score_desc = Column(String, nullable=False)
    total_positive = Column(Integer, nullable=False)
    total_negative = Column(Integer, nullable=False)
    total_reviews = Column(Integer, nullable=False)
    last_scraped = Column(BigInteger, nullable=False)

    reviews = relationship("Review", back_populates="game")
    user_stats = relationship(
        "UserGameStat",
        back_populates="game",
        cascade="save-update, merge",
    )
