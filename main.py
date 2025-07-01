"""Main entry point for manual test."""

import asyncio

# from src import scraper
from src.container import Container


async def main():
    """Main function for manual testing."""
    # app_id = 570  # Example app_id for testing
    # num_reviews = await scraper.scrape_reviews(app_id)
    # print(f"Number of reviews gathered for app_id {app_id}: {num_reviews}")
    container = Container()
    container.config.from_json("local.config.json")
    print("Container loaded with configuration:", container.config())


if __name__ == "__main__":
    asyncio.run(main())
