# country-explorer

Country Explorer is an interactive Python command-line application that retrieves live country information from the [countries.dev](https://countries.dev/) API.

Users can search for countries by full or partial name, filter countries by region, and view formatted information such as population, area, languages, and currencies.

## Features

- Fetches live country data from the countries.dev API
- Searches countries by full or partial name
- Supports case-insensitive searches
- Filters countries by region
- Displays all available regions
- Allows multiple actions during one session
- Formats population and area values for readability
- Handles missing or invalid country fields
- Handles network, HTTP, and JSON errors
- Exits gracefully through the menu or keyboard interruption

## Country Information Displayed

The application displays:

- Country name
- Capital
- Region
- Subregion
- Population
- Area
- Languages
- Currencies

## Technologies

- Python 3
- `requests`
- countries.dev API
- Git and GitHub

## Project Structure

```text
country-explorer-cli/
├── api.py
├── countries.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

# api.py

Handles communication with the countries.dev API, including:

- Sending the HTTP request
- Passing query parameters
- Setting a request timeout
- Validating HTTP responses
- Parsing JSON
- Handling API and network errors

# countries.py

Contains functions for:

- Transforming raw API responses
- Extracting nested language data
- Extracting nested currency data
- Searching countries by name
- Filtering countries by region
- Formatting country information

# main.py

Contains the command-line interface, including:

- Loading country data
- Displaying the main menu
- Handling user input
- Displaying search results
- Displaying region-filter results
- Gracefully exiting the application

## Installation
1. Clone the repository
```text
git clone https://github.com/sumanbista/country-explorer.git

cd country-explorer
```

2. Create a virtual environment

macOS or Linux:
```text
python3 -m venv .venv

source .venv/bin/activate
```

Windows PowerShell:
```text
python -m venv .venv

.venv\Scripts\Activate.ps1
```
Windows Command Prompt:
```text
python -m venv .venv

.venv\Scripts\activate
```

3. Install dependencies
```text
pip install -r requirements.txt
```
Usage

Run the application from the project root:
```text
python3 main.py
```

On systems where Python is available through python:
```text
python main.py
```
The application loads country data and displays the following menu:

Country Explorer Menu
----------------------------------------
1. Search for a country by name
2. Filter countries by region
3. Exit
Example: Search by Country Name
Choose an option: 1

Enter a full or partial country name: Nepal

Found 1 matching country or countries:

Result 1
----------------------------------------
```text
Name: Nepal
Capital: Kathmandu
Region: Asia
Subregion: Southern Asia
Population: 29,136,808
Area: 147,181.00 km²
Languages: Nepali
Currencies: Nepalese rupee
```

The exact values may change if the API dataset is updated.

Partial and case-insensitive searches are supported.

Examples:
```text
nepal
NEPAL
united
```

A partial search such as united may return multiple countries.

Example: Filter by Region
Choose an option: 2

Available regions:
- Africa
- Americas
- Asia
- Europe
- Oceania

Enter a region from the list above: Asia

The application then displays all matching countries in alphabetical order.

Region input is case-insensitive, so these values behave the same:
```text
Asia
asia
ASIA
```

# Error Handling

The application handles:
- Internet connection failures
- API request timeouts
- HTTP error responses
- Invalid JSON responses
- Unexpected API response formats
- Empty menu input
- Invalid menu selections
- Empty country searches
- Empty region selections
- Searches with no matching countries
- Missing or null country fields
- Keyboard interruption with Ctrl + C
- End-of-file input

Errors are displayed as readable messages instead of raw Python tracebacks.

# API

This project uses the countries.dev countries endpoint:
```text
https://countries.dev/countries
```

The request includes a fields query parameter so the API returns only the data needed by the application:
```text
name
capital
region
subregion
population
area
languages
currencies
```
No API key is required.