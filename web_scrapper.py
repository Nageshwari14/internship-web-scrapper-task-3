import requests
from bs4 import BeautifulSoup

def scrape_headlines(url="https://www.bbc.com/news", output_file="headlines.txt"):
    """
    Scrapes news headlines from the given URL and saves them to a text file.
    
    Args:
        url (str): The news website URL to scrape.
        output_file (str): The file where headlines will be saved.
    """
    try:
        # Step 1: Fetch HTML content
        response = requests.get(url)
        response.raise_for_status()  # Raise error if request failed

        # Step 2: Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Step 3: Extract headlines from <h2> tags
        headlines = [h2.get_text(strip=True) for h2 in soup.find_all("h2") if h2.get_text(strip=True)]

        if not headlines:
            print("No headlines found. Try a different tag or website.")
            return

        # Step 4: Save headlines into a text file (overwrite each run)
        with open(output_file, "w", encoding="utf-8") as f:
            for i, hl in enumerate(headlines, start=1):
                f.write(f"{i}. {hl}\n")

        print(f" Headlines scraped and saved to '{output_file}'")

    except requests.exceptions.RequestException as e:
        print(f" Error fetching the webpage: {e}")


if __name__ == "__main__":
    scrape_headlines()
