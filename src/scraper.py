"""Scraper module for gathering reviews from Steam API."""

from .dto_handler import (
    create_steam_review_response_dto as steam_response_dto,
    create_persistance_dto_from_response_dto as persistance_create_dto,
)
from .database_manager import DatabaseManager
from .http_client_manager import HttpClientManager


async def scrape_reviews(
    app_id: int, http_manager: HttpClientManager, db_manager: DatabaseManager
) -> int:
    """Main function to scrape reviews from Steam.

    Args:
        app_id (int): Steam's Application ID for which to scrape reviews.

    Returns:
        gathered_review (int): The number of reviews gathered for the specified app_id.
    """
    http_conn = http_manager.get_client("default")
    # db_conn = db_manager.get_connection("default")

    base_url = f"https://store.steampowered.com/appreviews/{app_id}"
    params = "?json=1&filter=recent&language=all"
    # cursor = "*"

    review_gathered = 0

    response = steam_response_dto(await http_conn.get(base_url + params))
    if response.success == 1:
        review_gathered = len(response.reviews)
        persistance_dto = persistance_create_dto(app_id=app_id, response_dto=response)
        print(f"{persistance_dto}")

    return review_gathered
