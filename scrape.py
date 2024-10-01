import requests
from bs4 import BeautifulSoup

# Function to scrape headlines from Al Jazeera homepage
def scrape_aljazeera_headlines(url):
    try:
        # Send an HTTP request to the Al Jazeera website
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the page content with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find and extract headlines (usually wrapped in <h2> or <h3> tags)
            headlines = soup.find_all('h3', class_='gc__title')  # Al Jazeera uses 'gc__title' class for headlines
            
            print("Top Headlines on Al Jazeera:")
            for i, headline in enumerate(headlines, start=1):
                print(f"{i}. {headline.text.strip()}")

        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

# URL of the Al Jazeera homepage
url = "https://www.aljazeera.com/"
scrape_aljazeera_headlines(url)
