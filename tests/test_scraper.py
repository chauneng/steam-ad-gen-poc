"""Test the review crawler functionality."""
import inspect
from src import scraper


def test_scrape_reviews_exists_and_callable():
    """Test that the 'scrape_reviews' function exists and is callable."""

    assert hasattr(
        scraper, "scrape_reviews"
    ), "scrape_reviews is not defined in src.scraper"

    assert callable(scraper.scrape_reviews), "scrape_reviews should be callable"


def test_scrape_reviews_signature():
    """Test that the 'scrape_reviews' function has the expected signature."""

    sig = inspect.signature(scraper.scrape_reviews)
    params = list(sig.parameters.keys())
    assert "app_id" in params, "scrape_reviews is missing the 'app_id' parameter"


def test_scrape_reviews_types():
    """Test that the 'scrape_reviews' function has the expected parameter types."""

    sig = inspect.signature(scraper.scrape_reviews)
    param = sig.parameters["app_id"]

    assert param.annotation == int, "The 'app_id' parameter should be of type int"


def test_scrape_reviews_return_type():
    """Test that the 'scrape_reviews' function returns an int."""

    example_app_id = 570  # Example app_id for testing
    result = scraper.scrape_reviews(example_app_id)
    assert isinstance(result, int), "scrape_reviews should return an int"
    assert result >= 0, "The number of reviews gathered should be non-negative"
