"""Entry point for the Country Explorer CLI."""

from api import fetch_countries
from typing import Any

from countries import (
    find_countries_by_name,
    format_country,
    transform_countries,
    filter_countries_by_region,
    get_available_regions
)


def display_countries(countries: list[dict[str, Any]],heading: str,) -> None:
    """Display a collection of countries in a readable format.

    Args:
        countries: Country dictionaries to display.
        heading: Heading shown before the results.
    """
    if not countries:
        print("\nNo matching countries were found.")
        return

    print(f"\n{heading}")

    for index, country in enumerate(countries, start=1):
        print(f"\nResult {index}")
        print("-" * 40)
        print(format_country(country))

def handle_country_search(countries: list[dict[str, Any]],) -> None:
    """Prompt the user to search for countries by name.

    Args:
        countries: Normalized country dictionaries.
    """
    search_term = input(
        "\nEnter a full or partial country name: "
    ).strip()

    if not search_term:
        print("Please enter a country name.")
        return

    matches = find_countries_by_name(countries, search_term)

    display_countries(
        matches,
        f"Found {len(matches)} matching country or countries:",
    )


def handle_region_filter(countries: list[dict[str, Any]],) -> None:
    """Prompt the user to filter countries by region.

    Args:
        countries: Normalized country dictionaries.
    """
    regions = get_available_regions(countries)

    if not regions:
        print("\nNo region data is available.")
        return

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

    display_countries(
        matches,
        f"Found {len(matches)} countries in {selected_region.title()}:",
    )


def display_menu() -> None:
    """Display the main application menu."""
    print("\nCountry Explorer Menu")
    print("-" * 40)
    print("1. Search for a country by name")
    print("2. Filter countries by region")
    print("3. Exit")


def run_menu(countries: list[dict[str, Any]],) -> None:
    """Run the interactive menu until the user chooses to exit.

    Args:
        countries: Normalized country dictionaries.
    """
    while True:
        display_menu()

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            handle_country_search(countries)
        elif choice == "2":
            handle_region_filter(countries)
        elif choice == "3":
            print("\nThank you for using Country Explorer.")
            break
        else:
            print(
                "\nInvalid selection. Please choose 1, 2, or 3."
            )


def main() -> None:
    """Fetch country data and display a sample of the country data."""
    print("Country Explorer")
    print("=" * 40)
    print("Loading country data...")

    try:
        raw_countries = fetch_countries()
        
    except RuntimeError as error:
        print(f"Error: {error}")
        return

    countries = transform_countries(raw_countries)

    print(f"Successfully loaded {len(countries)} countries.")

    try:
        run_menu(countries)
    except (KeyboardInterrupt, EOFError):
        print("\n\nCountry Explorer closed.")

if __name__ == "__main__":
    main()