"""Functions for retrieving country data from the countries.dev API."""

from typing import Any

import requests


BASE_URL = "https://countries.dev"
COUNTRIES_ENDPOINT = f"{BASE_URL}/countries"

COUNTRY_FIELDS = (
    "name",
    "capital",
    "region",
    "subregion",
    "population",
    "area",
    "languages",
    "currencies",
)


def fetch_countries(
    fields: tuple[str, ...] = COUNTRY_FIELDS,
) -> list[dict[str, Any]]:
    """Fetch countries from the countries.dev API.

    Args:
        fields: Country fields that should be included in the API response.

    Returns:
        A list of dictionaries containing raw country data.

    Raises:
        RuntimeError: If the request fails, returns invalid JSON, or returns
            an unexpected data structure.
    """
    params = {
        "fields": ",".join(fields),
    }

    try:
        response = requests.get(
            COUNTRIES_ENDPOINT,
            params=params,
            timeout=10,
        )
        response.raise_for_status()
    except requests.Timeout as error:
        raise RuntimeError(
            "The country API took too long to respond."
        ) from error
    except requests.ConnectionError as error:
        raise RuntimeError(
            "Unable to connect to the country API. Check your internet connection."
        ) from error
    except requests.HTTPError as error:
        raise RuntimeError(
            f"The country API returned an error: {response.status_code}."
        ) from error
    except requests.RequestException as error:
        raise RuntimeError(
            "An unexpected error occurred while requesting country data."
        ) from error

    try:
        data = response.json()
    except requests.JSONDecodeError as error:
        raise RuntimeError(
            "The country API returned invalid JSON data."
        ) from error

    if not isinstance(data, list):
        raise RuntimeError(
            "The country API returned an unexpected response format."
        )

    return data