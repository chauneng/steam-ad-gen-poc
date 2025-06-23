"""Property-based tests for SteamReviewsResponse DTO using Hypothesis."""

from hypothesis import given, strategies as st

from src.dto.steam_reviews import SteamReviewsResponse

success_strat = st.integers(min_value=0, max_value=1)

query_summary_strat = st.fixed_dictionaries(
    {
        "num_reviews": st.integers(min_value=0, max_value=100),
        "review_score": st.integers(min_value=0, max_value=10),
        "review_score_desc": st.sampled_from(
            ["Very Positive", "Positive", "Mixed", "Negative", "Very Negative"]
        ),
        "total_positive": st.integers(min_value=0, max_value=100_000),
        "total_negative": st.integers(min_value=0, max_value=100_000),
        "total_reviews": st.integers(min_value=0, max_value=100_000),
    }
)

author_strat = st.fixed_dictionaries(
    {
        "steamid": st.text(
            alphabet=st.characters(min_codepoint=48, max_codepoint=57), min_size=1
        ),
        "num_games_owned": st.integers(min_value=0, max_value=5000),
        "num_reviews": st.integers(min_value=0, max_value=1000),
        "playtime_forever": st.integers(min_value=0, max_value=10**7),
        "playtime_last_two_weeks": st.integers(min_value=0, max_value=10**6),
        "playtime_at_review": st.integers(min_value=0, max_value=10**7),
        "last_played": st.integers(min_value=0, max_value=2**31),
    }
)

review_strat = st.fixed_dictionaries(
    {
        "recommendationid": st.text(
            alphabet=st.characters(min_codepoint=48, max_codepoint=57), min_size=1
        ),
        "author": author_strat,
        "language": st.sampled_from(["english", "german", "russian", "spanish"]),
        "review": st.text(min_size=0, max_size=200),
        "timestamp_created": st.integers(min_value=0, max_value=2**31),
        "timestamp_updated": st.integers(min_value=0, max_value=2**31),
        "voted_up": st.booleans(),
        "votes_up": st.integers(min_value=0, max_value=1000),
        "votes_funny": st.integers(min_value=0, max_value=1000),
        "weighted_vote_score": st.floats(
            min_value=0, max_value=1, allow_nan=False, allow_infinity=False
        ),
        "comment_count": st.integers(min_value=0, max_value=100),
        "steam_purchase": st.booleans(),
        "received_for_free": st.booleans(),
        "written_during_early_access": st.booleans(),
        "primarily_steam_deck": st.booleans(),
    }
)

steam_reviews_strat = st.fixed_dictionaries(
    {
        "success": success_strat,
        "query_summary": query_summary_strat,
        "reviews": st.lists(review_strat, min_size=0, max_size=10),
        "cursor": st.text(min_size=1, max_size=32),
    }
)


@given(data=steam_reviews_strat)
def test_steam_reviews_parse_roundtrip(data):
    """Test that SteamReviewsResponse can be parsed and serialized correctly."""
    resp = SteamReviewsResponse.model_validate(data)

    # Check that the response is valid
    assert isinstance(resp, SteamReviewsResponse)
    assert isinstance(resp.success, int)
    assert 0 <= resp.success <= 1

    # round-trip serialization
    serialized = resp.model_dump_json()
    resp2 = SteamReviewsResponse.model_validate_json(serialized)
    assert resp2 == resp
