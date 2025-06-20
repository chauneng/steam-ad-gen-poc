"""Create Data Transfer Objects for handling informations between layers."""

from httpx import Response

from .dto.steam_reviews import SteamReviewsResponse


def create_steam_review_dto(data: Response) -> SteamReviewsResponse:
    """
    Create a Data Transfer Object (DTO) from the Steam API's HTTP response data.

    Args:
        data (Response): The HTTP response containing the data.

    Returns:
        SteamReviewsResponse: The DTO containing the parsed data.
    """
    return SteamReviewsResponse.model_validate(data.json())
