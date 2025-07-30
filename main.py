"""Main entry point for manual test."""

import asyncio
import sys

from sqlalchemy import text

# from src import scraper
from src.container import Container
from src.migration import run_migrations

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def main():
    """Main function for manual testing."""
    # app_id = 570  # Example app_id for testing
    # num_reviews = await scraper.scrape_reviews(app_id)
    # print(f"Number of reviews gathered for app_id {app_id}: {num_reviews}")

    # Initialize basic components
    container = Container()
    container.config.from_json("local.config.json")
    db_manager = container.db_manager()
    db_config = container.config.database()
    engine = db_manager.create_asynchronous_connection("default", db_config)
    run_migrations(db_manager.create_db_url(db_config), "alembic.ini")

    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        scalar = result.scalar()
        print("SELECT 1 결과:", scalar)
    await db_manager.dispose_all_connections()


if __name__ == "__main__":
    asyncio.run(main())
