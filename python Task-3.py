# Python-Tak-3
import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises HTTPError if status code is not 200
        soup = BeautifulSoup(response.text, 'html.parser')
        headline_tags = soup.find_all('h3')
        headlines = [tag.text.strip() for tag in headline_tags if tag.text.strip()]
        if len(headlines) < 5:
            h2_tags = soup.find_all('h2')
            headlines += [tag.text.strip() for tag in h2_tags if tag.text.strip()]
        with open('headlines.txt', 'w', encoding='utf-8') as f:
            for headline in headlines:
                f.write(headline + '\n')
        print(f"Extracted {len(headlines)} headlines. Saved to headlines.txt")
    except Exception as e:
        print(f"Error: {e}")
fetch_headlines('https://www.eenadu.net/')

