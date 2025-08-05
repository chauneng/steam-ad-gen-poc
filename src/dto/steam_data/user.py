"""User information for a Steam review."""

from pydantic import BaseModel, ConfigDict

from .user_game_stat import UserGameStat


class User(BaseModel):
    """User information for a Steam review."""
    
    steamid: int
    num_games_owned: int
    num_reviews: int
    game_stats: UserGameStat

    model_config = ConfigDict(populate_by_name=True)

    model_validator(mode="before")

    def check_game_stats(self, values: dict) -> UserGameStat:
        """Assemble UserGameStat from response data."""

        playtime_forever = values.get("playtime_forever", 0)
        playtime_last_two_weeks = values.get("playtime_last_two_weeks", 0)
        playtime_at_review = values.get("playtime_at_review", 0)
        last_played = values.get("last_played", 0)
