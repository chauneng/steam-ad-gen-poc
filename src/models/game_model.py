"""Game model for Steam games."""

from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from src.models.base_model import BaseModel, CommonMixin, TimestampMixin


class Game(CommonMixin, TimestampMixin, BaseModel):
    """Represents a Steam game with its metadata and reviews."""

    id = Column(Integer, primary_key=True)

    query_summary = relationship(
        "ReviewQueryResponse",
        back_populates="game",
        cascade="save-update, merge",
    )
    reviews = relationship("Review", back_populates="game")
    user_stats = relationship(
        "UserGameStat",
        back_populates="game",
        cascade="save-update, merge",
    )
