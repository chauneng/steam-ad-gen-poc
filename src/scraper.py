"""Scraper module for gathering reviews from Steam API."""

from .dto_handler import (
    create_steam_review_response_dto as steam_response_dto,
    create_persistance_dto_from_response_dto as persistance_create_dto,
)
from .database_manager import DatabaseManager
from .http_client_manager import HttpClientManager
from .repositories import GameRepo
from .repositories import QuerySummaryRepo


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
    db_session_factory = db_manager.get_session_factory("default")

    base_url = f"https://store.steampowered.com/appreviews/{app_id}"
    params = "?json=1&filter=recent&language=all"

    async with db_session_factory() as session:
        querysummary_repo = QuerySummaryRepo(session)
        game_repo = GameRepo(session)

        previous_summary = await querysummary_repo.get_query_summary(app_id)
        if previous_summary is not None:
            cursor = previous_summary.cursor
            params += f"&cursor={cursor}"
        else:
            await game_repo.add_game(app_id)

        print(f"Fetching reviews from URL: {base_url + params}")
        response = steam_response_dto(await http_conn.get(base_url + params))

        review_gathered = 0

        if response.success == 0:
            return review_gathered

        review_gathered += len(response.reviews)
        persistance_dto = persistance_create_dto(app_id=app_id, response_dto=response)
        await querysummary_repo.add_query_summary(persistance_dto.query_summary)

    return review_gathered
