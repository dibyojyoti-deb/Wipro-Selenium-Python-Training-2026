import requests
import json
from bs4 import BeautifulSoup


def scrape_webpage():
    url = "https://www.w3schools.com/html/html_tables.asp"

    try:
        # 1. Fetch HTML webpage
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # 2. Parse HTML using BeautifulSoup with lxml parser
        soup = BeautifulSoup(response.text, "lxml")

        # 3. Extract page title
        page_title = soup.title.string.strip() if soup.title else "No title found"

        # Extract all hyperlinks
        links = []
        for link in soup.find_all("a", href=True):
            links.append(link["href"])

        # Extract specific table data (first HTML table)
        table_data = []
        table = soup.find("table")

        if table:
            rows = table.find_all("tr")
            for row in rows[1:]:  # Skip header row
                columns = row.find_all("td")
                if columns:
                    table_data.append({
                        "Company": columns[0].get_text(strip=True),
                        "Contact": columns[1].get_text(strip=True),
                        "Country": columns[2].get_text(strip=True)
                    })

        # 4. Convert extracted data into JSON format
        extracted_data = {
            "title": page_title,
            "links": links,
            "table_data": table_data
        }

        # 5. Save output into a JSON file
        with open("scraped_data.json", "w", encoding="utf-8") as file:
            json.dump(extracted_data, file, indent=4)

        print("Webpage data successfully scraped and saved to scraped_data.json")

    except requests.exceptions.HTTPError as http_error:
        print(f"HTTP error occurred: {http_error}")

    except requests.exceptions.ConnectionError:
        print("Error: Failed to connect to the webpage")

    except requests.exceptions.Timeout:
        print("Error: Request timed out")

    except Exception as error:
        print(f"Unexpected error occurred: {error}")


if __name__ == "__main__":
    scrape_webpage()
