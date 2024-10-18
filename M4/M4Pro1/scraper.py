# Webscraping
# 10/18/24
# CSC221 M4Pro
# Mahamed Abdel




import requests
from bs4 import BeautifulSoup

# Function to scrape songs for a specific year
def scrape_songs_from_year(year):
    url = f"https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_{year}"
    songs = []
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Locate the table with the song data
        table = soup.find('table', {'class': 'wikitable'})
        if not table:
            raise ValueError(f"No data found for year {year}")
        
        # Extract the rows of the table (skipping the header)
        rows = table.find_all('tr')[1:]

        # Loop over rows to extract rank, title, and artist
        for row in rows:
            columns = row.find_all('td')
            if len(columns) >= 3:
                rank = columns[0].text.strip()
                title = columns[1].text.strip().strip('"')  # Remove quotes around title
                artist = columns[2].text.strip()
                songs.append((rank, title, artist, year))
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for year {year}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return songs
