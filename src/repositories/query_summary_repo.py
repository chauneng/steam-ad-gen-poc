from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound
from ..models import ReviewQuerySummary as RQEntity
from ..dto.steam_data import ReviewQuerySummaryDTO
from ..dto.steam_persistance import UpsertReviewQuerySummaryDTO
from typing import Optional

"""
Abstract repository for managing game-related data.
"""


class QuerySummaryRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_query_summary(self, game_id: int) -> Optional[ReviewQuerySummaryDTO]:
        """Retrieve a game data by its ID."""
        try:
            statement = (
                select(RQEntity)
                .where(RQEntity.game_id == game_id)
                .order_by(desc(RQEntity.updated_at))
                .limit(1)
            )
            result = await self.session.scalar(statement)
            if not result:
                return None
            return ReviewQuerySummaryDTO.model_validate(result)
        except NoResultFound:
            return None

    async def add_query_summary(self, upsert_dto: UpsertReviewQuerySummaryDTO) -> bool:
        self.session.add(RQEntity(**upsert_dto.model_dump(exclude_unset=True)))
        try:
            await self.session.commit()
            return True
        except Exception as e:
            await self.session.rollback()
            print(f"Error adding game: {e}")
            return False
