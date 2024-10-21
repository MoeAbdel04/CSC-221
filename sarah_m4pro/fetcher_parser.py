import requests
from bs4 import BeautifulSoup

# Function to fetch the page content from the Wikipedia URL
def fetch_page_content(year):
    url = f"https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_{year}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for bad HTTP responses
        return response.content
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred for year {year}: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred for year {year}: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

# Function to parse the song data from the HTML content
def parse_song_data(page_content, year):
    soup = BeautifulSoup(page_content, "html.parser")
    
    # Find the table containing the data
    table = soup.find("table", {"class": "wikitable"})
    
    # Create a list to store the data
    song_data = []
    
    if table:
        rows = table.find_all("tr")[1:]  # Skip the header row
        for row in rows:
            cells = row.find_all("td")
            if len(cells) >= 2:
                rank = cells[0].text.strip()
                title = cells[1].text.strip().strip('"')  # Remove quotes around titles
                artist = cells[2].text.strip()
                
                # Append a tuple with (rank, title, artist, year)
                song_data.append((rank, title, artist, year))
    else:
        print(f"No data table found for year {year}.")
    
    return song_data
