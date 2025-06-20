""" HTTP client for making requests and handling responses for other modules."""

from typing import Optional

import httpx


async def get(url: str, params: Optional[dict] = None) -> httpx.Response:
    """Make a GET request to the specified URL with optional parameters.

    Args:
        url (str): The URL to send the GET request to.
        params (dict, optional): Optional query parameters to include in the request.

    Returns:
        httpx.Response: The response object from the GET request.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response
