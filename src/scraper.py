"""Scraper module for gathering reviews from Steam API."""
from . import http_client


async def scrape_reviews(app_id: int) -> int:
    """Main function to scrape reviews from Steam.

    Args:
        app_id (int): Steam's Application ID for which to scrape reviews.

    Returns:
        gathered_review (int): The number of reviews gathered for the specified app_id.
    """

    base_url = f"https://store.steampowered.com/appreviews/{app_id}?json=1"
    response = (await http_client.get(base_url)).json()
    print(response)

    review_gathered: int = 0

    return review_gathered
