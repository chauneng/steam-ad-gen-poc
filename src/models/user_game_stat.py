"""User Game Statistics Model"""

from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import relationship

from src.models.base_model import BaseModel, CommonMixin


class UserGameStat(CommonMixin, BaseModel):
    """
    Represents a user's game statistics on Steam, such as playtime and last played time.
    """

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("user.id"), nullable=False)
    game_id = Column(BigInteger, ForeignKey("game.id"), nullable=False)

    playtime_forever = Column(TIMESTAMP, nullable=False)
    playtime_last_two_weeks = Column(TIMESTAMP, nullable=False)
    playtime_at_review = Column(TIMESTAMP, nullable=False)
    last_played = Column(TIMESTAMP, nullable=False)

    user = relationship(
        "User",
        back_populates="game_stats",
        cascade="save-update, merge",
        foreign_keys=[user_id],
    )
    game = relationship(
        "Game",
        back_populates="user_stats",
        cascade="save-update, merge",
        foreign_keys=[game_id],
    )
