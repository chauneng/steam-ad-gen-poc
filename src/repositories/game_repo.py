from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound
from ..models import Game as GameEntity
from ..dto.steam_data import GameDTO
from typing import Optional

"""
Abstract repository for managing game-related data.
"""


class GameRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_game(self, game_id: int) -> Optional[GameDTO]:
        """Retrieve a game data by its ID."""
        try:
            await self.session.get_one(GameEntity, game_id)

            return GameDTO.model_validate(
                await self.session.get_one(GameEntity, game_id)
            )
        except NoResultFound:
            return None

    async def add_game(self, game_id: int) -> bool:
        self.session.add(GameEntity(id=game_id))
        try:
            await self.session.commit()
            return True
        except Exception as e:
            await self.session.rollback()
            print(f"Error adding game: {e}")
            return False
