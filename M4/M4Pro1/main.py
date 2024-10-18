from scraper import scrape_songs_from_year
from file_writer import save_songs_to_csv

def main():
    try:
        start_year = int(input("Enter the start year: "))
        end_year = int(input("Enter the end year: "))
        all_songs = []

        for year in range(start_year, end_year + 1):
            print(f"Fetching songs for {year}...")
            songs = scrape_songs_from_year(year)
            all_songs.extend(songs)
        
        if all_songs:
            save_songs_to_csv("top_songs.csv", all_songs)
        else:
            print("No data to save.")
    except ValueError:
        print("Invalid year input. Please enter valid years.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
