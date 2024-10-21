from scraper import scrape_range_of_years
from csv_saver import save_to_csv, get_year_range

# Main function that controls the flow of the program
def main():
    start_year, end_year = get_year_range()
    
    if start_year and end_year:
        # Define the output filename
        output_file = f"top_songs_{start_year}_{end_year}.csv"
        
        # Scrape data for the specified range of years
        all_data = scrape_range_of_years(start_year, end_year)
        
        # Save the data to CSV
        save_to_csv(all_data, output_file)

# Run the main function
if __name__ == "__main__":
    main()
