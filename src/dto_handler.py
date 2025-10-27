"""Create Data Transfer Objects for handling informations between layers."""

from httpx import Response

from .dto.steam_persistance.game.upsert_game import UpsertGameDTO
from .dto.steam_persistance.review.upsert_query_summary import (
    UpsertReviewQuerySummaryDTO,
)
from .dto.steam_persistance.review.upsert_review import UpsertReviewDTO
from .dto.steam_persistance.upsert_response import UpsertResponseDTO
from .dto.steam_persistance.user.upsert_user import UpsertUserDTO
from .dto.steam_persistance.user.upsert_user_game_stat import UpsertUserGameStatsDTO
from .dto.steam_reviews_response import SteamReviewsResponse


def create_steam_review_response_dto(data: Response) -> SteamReviewsResponse:
    """
    Create a Data Transfer Object (DTO) from the Steam API's HTTP response data.

    Args:
        data (Response): The HTTP response containing the data.

    Returns:
        SteamReviewsResponse: The DTO containing the parsed data.
    """
    return SteamReviewsResponse.model_validate(data.json())


def create_persistance_dto_from_response_dto(
    app_id: int,
    response_dto: SteamReviewsResponse,
) -> UpsertResponseDTO:
    """
    Create a persistence DTO from the response DTO.

    Args:
        response_dto (SteamReviewsResponse): The response DTO to convert.

    Returns:
        UpsertResponseDTO: The persistence DTO.
    """
    game_dto = UpsertGameDTO(id=app_id)
    query_summary = UpsertReviewQuerySummaryDTO(
        id=None,
        game_id=app_id,
        num_reviews=response_dto.query_summary.num_reviews,
        review_score=response_dto.query_summary.review_score,
        review_score_desc=response_dto.query_summary.review_score_desc,
        total_positive=response_dto.query_summary.total_positive,
        total_negative=response_dto.query_summary.total_negative,
        total_reviews=response_dto.query_summary.total_reviews,
        cursor=response_dto.cursor,
    )
    user_list = []
    review_list = []
    user_stats_list = []
    for review in response_dto.reviews:
        user = UpsertUserDTO(
            id=review.author.steamid,
            num_games_owned=review.author.num_games_owned,
            num_reviews=review.author.num_reviews,
        )
        user_list.append(user)

        review_dto = UpsertReviewDTO(
            id=review.recommendationid,
            user_id=review.author.steamid,
            game_id=app_id,
            language=review.language,
            review_text=review.review,
            created_at=review.timestamp_created,
            updated_at=review.timestamp_updated,
            voted_up=review.voted_up,
            votes_up=review.votes_up,
            votes_funny=review.votes_funny,
            weighted_vote_score=review.weighted_vote_score,
            comment_count=review.comment_count,
            steam_purchase=review.steam_purchase,
            received_for_free=review.received_for_free,
            written_during_early_access=review.written_during_early_access,
            primarily_steam_deck=review.primarily_steam_deck,
        )
        review_list.append(review_dto)

        user_stats = UpsertUserGameStatsDTO(
            user_id=review.author.steamid,
            game_id=app_id,
            playtime_forever=review.author.playtime_forever,
            playtime_last_two_weeks=review.author.playtime_last_two_weeks,
            playtime_at_review=review.author.playtime_at_review,
            last_played=review.author.last_played,
        )
        user_stats_list.append(user_stats)

    dto = UpsertResponseDTO(
        game=game_dto,
        users=user_list,
        user_stats=user_stats_list,
        reviews=review_list,
        query_summary=query_summary,
    )
    return dto
