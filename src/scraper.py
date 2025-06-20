"""Scraper module for gathering reviews from Steam API."""

from . import http_client
from .dto_handler import create_steam_review_dto


async def scrape_reviews(app_id: int) -> int:
    """Main function to scrape reviews from Steam.

    Args:
        app_id (int): Steam's Application ID for which to scrape reviews.

    Returns:
        gathered_review (int): The number of reviews gathered for the specified app_id.
    """

    base_url = f"https://store.steampowered.com/appreviews/{app_id}?json=1"

    review_gathered = 0

    response = create_steam_review_dto(await http_client.get(base_url))
    if response.success == 1:
        review_gathered = len(response.reviews)
        # Print summary for debugging purposes
        print(response.query_summary)

    return review_gathered
