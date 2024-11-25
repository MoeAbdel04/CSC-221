# Airline
# 11/22/24
# CSC221 M6Pro
# Mahamed Abdel

from analysis import load_data, add_sentiment, add_day_of_week, summarize_and_plot

def display_menu():
    """Display the program menu."""
    print("\nMenu Options:")
    print("1. Airline Summary and Chart")
    print("2. Sentiment Summary and Chart")
    print("3. Sentiment Per Airline Summary and Chart")
    print("4. Overall Sentiment and Airline Summary and Chart")
    print("5. Day and Sentiment Summary and Chart")
    print("6. Exit")

def main():
    file_path = "Tweets(1).xlsx"  # Adjust the path to your local file location
    try:
        # Load and preprocess data
        data = load_data(file_path)
        data = add_sentiment(data)
        data = add_day_of_week(data)
        
        while True:
            display_menu()
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                print("\nAirline Summary and Chart...")
                summary = summarize_and_plot(data, "airline_name", "sentiment", "airline_analysis.png")
                print(summary)
            
            elif choice == "2":
                print("\nSentiment Summary and Chart...")
                summary = summarize_and_plot(data, "sentiment", "sentiment", "sentiment_analysis.png")
                print(summary)
            
            elif choice == "3":
                print("\nSentiment Per Airline Summary and Chart...")
                summary = summarize_and_plot(data, "airline_name", "sentiment", "airline_senti.png")
                print(summary)
            
            elif choice == "4":
                print("\nOverall Sentiment and Airline Summary and Chart...")
                summary = summarize_and_plot(data, "airline_name", "sentiment", "senti_air_per.png")
                print(summary)
            
            elif choice == "5":
                print("\nDay and Sentiment Summary and Chart...")
                summary = summarize_and_plot(data, "day_of_week", "sentiment", "day_senti.png")
                print(summary)
            
            elif choice == "6":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
