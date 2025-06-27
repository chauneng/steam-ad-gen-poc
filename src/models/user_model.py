"""User model for Steam users."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.models.base_model import BaseModel, CommonMixin


class User(CommonMixin, BaseModel):
    """Represents a Steam user with their metadata and reviews."""

    steamid = Column(String, primary_key=True)
    num_games_owned = Column(Integer, nullable=False)
    num_reviews = Column(Integer, nullable=False)

    reviews = relationship("Review", back_populates="author")
    game_stats = relationship(
        "UserGameStat",
        back_populates="user",
        cascade="save-update, merge",
    )
