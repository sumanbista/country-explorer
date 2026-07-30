"""Entry point for the Country Explorer CLI."""

from api import fetch_countries
from countries import (
    find_countries_by_name,
    format_country,
    transform_countries,
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

    search_term = input(
        "\nEnter a full or partial country name: "
    ).strip()

    if not search_term:
        print("Please enter a country name.")
        return

    matches = find_countries_by_name(countries, search_term)
    display_search_results(matches)

    # if not countries:
    #     print("No country data is available.")
    #     return

    # sample_country = countries[0]

    # print("\nSample country")
    # print("-" * 30)
    # print(f"Name: {sample_country['name']}")
    # print(f"Capital: {sample_country['capital']}")
    # print(f"Region: {sample_country['region']}")
    # print(f"Population: {sample_country['population']:,}")
    # print(f"Area: {sample_country['area']:,.2f} km²")
    # print(
    #     "Languages: "
    #     + (", ".join(sample_country["languages"]) or "Not available")
    # )
    # print(
    #     "Currencies: "
    #     + (", ".join(sample_country["currencies"]) or "Not available")
    # )


if __name__ == "__main__":
    main()