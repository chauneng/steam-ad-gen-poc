"""Review model for Steam reviews."""

from sqlalchemy import BigInteger, Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.models.base_model import (
    BaseModel,
    CommonMixin,
    SoftDeleteMixin,
    TimestampMixin,
)


class Review(CommonMixin, TimestampMixin, SoftDeleteMixin, BaseModel):
    """
    Represents a Steam review for a game.
    """

    recommendationid = Column(String, primary_key=True)
    game_id = Column(Integer, ForeignKey("game.id"), nullable=False)
    user_id = Column(String, ForeignKey("user.id"), nullable=False)

    language = Column(String, nullable=False)
    review_text = Column(String, nullable=False)
    timestamp_created = Column(BigInteger, nullable=False)
    timestamp_updated = Column(BigInteger, nullable=False)
    voted_up = Column(Boolean, nullable=False)
    votes_up = Column(Integer, nullable=False)
    votes_funny = Column(Integer, nullable=False)
    weighted_vote_score = Column(Float, nullable=False)
    comment_count = Column(Integer, nullable=False)
    steam_purchase = Column(Boolean, nullable=False)
    received_for_free = Column(Boolean, nullable=False)
    written_during_early_access = Column(Boolean, nullable=False)
    primarily_steam_deck = Column(Boolean, nullable=False)

    user = relationship(
        "User",
        back_populates="reviews",
        cascade="save-update, merge",
        foreign_keys=[user_id],
    )
    game = relationship(
        "Game",
        back_populates="reviews",
        cascade="save-update, merge",
        foreign_keys=[game_id],
    )
