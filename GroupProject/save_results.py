from data import decimal_guess_df, binary_guess_df, wildcard_df

def save_results():
    """ Function to save all results to CSV files. """
    
    # Debugging: print the DataFrame before saving
    print("\nSaving binary_guess_df to binary_guess.csv:")
    print(binary_guess_df)
    
    print("\nSaving decimal_guess_df to decimal_guess.csv:")
    print(decimal_guess_df)
    
    print("\nSaving wildcard_df to wildcard.csv:")
    print(wildcard_df)
    
    # Save the data to CSV files
    if not decimal_guess_df.empty:
        decimal_guess_df.to_csv("decimal_guess.csv", index=False)
        print("Saved decimal conversion results to 'decimal_guess.csv'.")
    else:
        print("No decimal conversion data to save.")
    
    if not binary_guess_df.empty:
        binary_guess_df.to_csv("binary_guess.csv", index=False)
        print("Saved binary conversion results to 'binary_guess.csv'.")
    else:
        print("No binary conversion data to save.")
    
    if not wildcard_df.empty:
        wildcard_df.to_csv("wildcard.csv", index=False)
        print("Saved subnet question results to 'wildcard.csv'.")
    else:
        print("No subnet question data to save.")
