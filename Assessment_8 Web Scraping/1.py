import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com'

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    print("Successfully created a Beautiful Soup object.")

    quotes = soup.find_all('div', class_='quote')

    print(f"\nFound {len(quotes)} quotes on the page.")

    for quote in quotes:
        text = quote.find('span', class_='text').text.strip()
        
        author = quote.find('small', class_='author').text.strip()
        
        tags = [tag.text for tag in quote.find('div', class_='tags').find_all('a', class_='tag')]
        
        print("\n---")
        print(f"Quote: {text}")
        print(f"Author: {author}")
        print(f"Tags: {', '.join(tags)}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")