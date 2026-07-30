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


def transform_countries(countries: list[dict[str, Any]],) -> list[dict[str, Any]]:
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


def find_countries_by_name(countries: list[dict[str, Any]], search_term: str,) -> list[dict[str, Any]]:
    """Find countries whose names contain the user's search term.

    The search is case-insensitive and supports partial names.

    Args:
        countries: Normalized country dictionaries.
        search_term: Full or partial country name entered by the user.

    Returns:
        A list of matching countries sorted alphabetically.
    """
    normalized_term = search_term.strip().casefold()

    if not normalized_term:
        return []

    matches = []

    for country in countries:
        name = country.get("name", "")

        if isinstance(name, str) and normalized_term in name.casefold():
            matches.append(country)

    return sorted(
        matches,
        key=lambda country: country.get("name", "").casefold(),
    )


def format_country(country: dict[str, Any]) -> str:
    """Create a readable multiline description of a country.

    Args:
        country: A normalized country dictionary.

    Returns:
        A formatted string containing the country's details.
    """
    languages = country.get("languages", [])
    currencies = country.get("currencies", [])

    language_text = (
        ", ".join(languages)
        if isinstance(languages, list) and languages
        else "Not available"
    )

    currency_text = (
        ", ".join(currencies)
        if isinstance(currencies, list) and currencies
        else "Not available"
    )

    population = country.get("population", 0)
    area = country.get("area", 0)

    return "\n".join(
        [
            f"Name: {country.get('name', 'Unknown')}",
            f"Capital: {country.get('capital', 'Not available')}",
            f"Region: {country.get('region', 'Not available')}",
            f"Subregion: {country.get('subregion', 'Not available')}",
            f"Population: {population:,}",
            f"Area: {area:,.2f} km²",
            f"Languages: {language_text}",
            f"Currencies: {currency_text}",
        ]
    )