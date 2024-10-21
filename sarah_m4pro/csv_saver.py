import pandas as pd

# Function to save the scraped data into a CSV file
def save_to_csv(data, filename):
    if data:
        # Convert the list of tuples to a DataFrame
        df = pd.DataFrame(data, columns=["Rank", "Title", "Artist", "Year"])
        # Save to CSV
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    else:
        print("No data to save.")

# Function to get input from the user for the range of years
def get_year_range():
    try:
        start_year = int(input("Enter the start year: "))
        end_year = int(input("Enter the end year: "))
        if start_year > end_year:
            raise ValueError("Start year cannot be greater than end year.")
        return start_year, end_year
    except ValueError as ve:
        print(f"Invalid input: {ve}")
        return None, None
