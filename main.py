"""Main entry point for manual test."""

import asyncio

from src import scraper


async def main():
    """Main function for manual testing. currently only tests the scraper."""
    app_id = 570  # Example app_id for testing
    num_reviews = await scraper.scrape_reviews(app_id)
    print(f"Number of reviews gathered for app_id {app_id}: {num_reviews}")


if __name__ == "__main__":
    asyncio.run(main())
