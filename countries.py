"""Functions for transforming and working with country data."""

from typing import Any


def extract_language_names(languages: Any) -> list[str]:
    """Extract language names from a raw API languages value.

    Args:
        languages: A value returned in the country's languages field.

    Returns:
        A list containing valid language names.
    """
    if not isinstance(languages, list):
        return []

    language_names = []

    for language in languages:
        if not isinstance(language, dict):
            continue

        name = language.get("name")

        if isinstance(name, str) and name.strip():
            language_names.append(name.strip())

    return language_names


def extract_currency_names(currencies: Any) -> list[str]:
    """Extract currency names from a raw API currencies value.

    Args:
        currencies: A value returned in the country's currencies field.

    Returns:
        A list containing valid currency names.
    """
    if not isinstance(currencies, list):
        return []

    currency_names = []

    for currency in currencies:
        if not isinstance(currency, dict):
            continue

        name = currency.get("name")

        if isinstance(name, str) and name.strip():
            currency_names.append(name.strip())

    return currency_names


def transform_country(country: dict[str, Any]) -> dict[str, Any]:
    """Convert a raw API country into a consistent application dictionary.

    Args:
        country: A raw country dictionary returned by countries.dev.

    Returns:
        A normalized country dictionary containing the fields used by the CLI.
    """
    name = country.get("name")
    capital = country.get("capital")
    region = country.get("region")
    subregion = country.get("subregion")
    population = country.get("population")
    area = country.get("area")

    return {
        "name": name.strip() if isinstance(name, str) and name.strip() else "Unknown",
        "capital": (
            capital.strip()
            if isinstance(capital, str) and capital.strip()
            else "Not available"
        ),
        "region": (
            region.strip()
            if isinstance(region, str) and region.strip()
            else "Not available"
        ),
        "subregion": (
            subregion.strip()
            if isinstance(subregion, str) and subregion.strip()
            else "Not available"
        ),
        "population": (
            population
            if isinstance(population, int) and not isinstance(population, bool)
            else 0
        ),
        "area": (
            area
            if isinstance(area, (int, float)) and not isinstance(area, bool)
            else 0
        ),
        "languages": extract_language_names(country.get("languages")),
        "currencies": extract_currency_names(country.get("currencies")),
    }


def transform_countries(
    countries: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Transform a list of raw country dictionaries.

    Args:
        countries: Raw country dictionaries returned by the API.

    Returns:
        A list of normalized country dictionaries.
    """
    transformed_countries = []

    for country in countries:
        if isinstance(country, dict):
            transformed_countries.append(transform_country(country))

    return transformed_countries