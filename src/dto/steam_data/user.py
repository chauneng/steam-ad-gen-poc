"""User information for a Steam review."""

from pydantic import BaseModel, ConfigDict

from .user_game_stat import UserGameStatDTO


class UserDTO(BaseModel):
    """User information for a Steam review."""

    steamid: int
    num_games_owned: int
    num_reviews: int
    game_stats: UserGameStatDTO

    model_config = ConfigDict(populate_by_name=True)
