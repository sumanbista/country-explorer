"""Entry point for the Country Explorer CLI."""

from api import fetch_countries
from countries import (
    find_countries_by_name,
    format_country,
    transform_countries,
    filter_countries_by_region,
    get_available_regions
)

def display_search_results(matches: list[dict], ) -> None:
    """Display countries returned by a name search.

    Args:
        matches: Country dictionaries matching the user's search.
    """
    if not matches:
        print("\nNo matching countries were found.")
        return

    print(f"\nFound {len(matches)} matching country or countries:")

    for index, country in enumerate(matches, start=1):
        print(f"\nResult {index}")
        print("-" * 40)
        print(format_country(country))


def display_region_results(countries: list[dict],region: str,) -> None:
    """Display countries belonging to a selected region.

    Args:
        countries: Countries matching the selected region.
        region: Region entered by the user.
    """
    if not countries:
        print(f"\nNo countries were found for the region '{region}'.")
        return

    print(f"\nFound {len(countries)} countries in {region.title()}:")

    for index, country in enumerate(countries, start=1):
        print(f"\nCountry {index}")
        print("-" * 40)
        print(format_country(country))


def main() -> None:
    """Fetch country data and display a sample of the country data."""
    print("Country Explorer")
    print("=" * 40)
    print("Loading country data...")

    try:
        raw_countries = fetch_countries()
        # print(countries[0])
    except RuntimeError as error:
        print(f"Error: {error}")
        return

    countries = transform_countries(raw_countries)

    print(f"Successfully loaded {len(countries)} countries.")

    # search_term = input(
    #     "\nEnter a full or partial country name: "
    # ).strip()

    # if not search_term:
    #     print("Please enter a country name.")
    #     return

    # matches = find_countries_by_name(countries, search_term)
    # display_search_results(matches)

    regions = get_available_regions(countries)

    print("\nAvailable regions:")

    for region in regions:
        print(f"- {region}")

    selected_region = input(
        "\nEnter a region from the list above: "
    ).strip()

    if not selected_region:
        print("Please enter a region.")
        return

    matches = filter_countries_by_region(
        countries,
        selected_region,
    )

    display_region_results(matches, selected_region)


if __name__ == "__main__":
    main()