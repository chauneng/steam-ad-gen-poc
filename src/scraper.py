"""Scraper module for gathering reviews from Steam API."""

from . import http_client
from .dto_handler import create_steam_review_response_dto, create_persistance_dto_from_response_dto


async def scrape_reviews(app_id: int) -> int:
    """Main function to scrape reviews from Steam.

    Args:
        app_id (int): Steam's Application ID for which to scrape reviews.

    Returns:
        gathered_review (int): The number of reviews gathered for the specified app_id.
    """

    base_url = f"https://store.steampowered.com/appreviews/{app_id}?json=1&filter=recent&language=all"

    review_gathered = 0

    response = create_steam_review_response_dto(await http_client.get(base_url))
    if response.success == 1:
        review_gathered = len(response.reviews)
        persistance_dto = create_persistance_dto_from_response_dto(
            app_id=app_id,
            response_dto=response
        )
        print(f"{persistance_dto}")

    return review_gathered
