"""Entry point for the Country Explorer CLI."""

from api import fetch_countries
from countries import transform_countries


def main() -> None:
    """Fetch country data and display a sample of the country data."""
    print("Loading country data...")

    try:
        raw_countries = fetch_countries()
        # print(countries[0])
    except RuntimeError as error:
        print(f"Error: {error}")
        return

    countries = transform_countries(raw_countries)

    print(f"Successfully loaded {len(countries)} countries.")

    if not countries:
        print("No country data is available.")
        return

    sample_country = countries[0]

    print("\nSample country")
    print("-" * 30)
    print(f"Name: {sample_country['name']}")
    print(f"Capital: {sample_country['capital']}")
    print(f"Region: {sample_country['region']}")
    print(f"Population: {sample_country['population']:,}")
    print(f"Area: {sample_country['area']:,.2f} km²")
    print(
        "Languages: "
        + (", ".join(sample_country["languages"]) or "Not available")
    )
    print(
        "Currencies: "
        + (", ".join(sample_country["currencies"]) or "Not available")
    )


if __name__ == "__main__":
    main()