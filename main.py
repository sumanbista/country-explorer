"""Entry point for the Country Explorer CLI."""

from api import fetch_countries


def main() -> None:
    """Fetch country data and display a loading confirmation."""
    print("Loading country data...")

    try:
        countries = fetch_countries()
        # print(countries[0])
    except RuntimeError as error:
        print(f"Error: {error}")
        return

    print(f"Successfully loaded {len(countries)} countries.")

    if countries:
        first_country = countries[0]
        print(f"Sample country: {first_country.get('name', 'Unknown')}")


if __name__ == "__main__":
    main()