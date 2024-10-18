import csv

# Function to save song data to a CSV file
def save_songs_to_csv(filename, data):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["#", "Title", "Artist", "Year"])  # Write header
            writer.writerows(data)
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")
