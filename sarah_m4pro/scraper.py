from fetcher_parser import fetch_page_content, parse_song_data

# Function to scrape the data for a specific year
def scrape_year(year):
    page_content = fetch_page_content(year)
    if page_content:
        return parse_song_data(page_content, year)
    else:
        return []

# Function to scrape the data for a range of years
def scrape_range_of_years(start_year, end_year):
    all_data = []
    
    for year in range(start_year, end_year + 1):
        print(f"Scraping data for {year}...")
        year_data = scrape_year(year)
        all_data.extend(year_data)
    
    return all_data
