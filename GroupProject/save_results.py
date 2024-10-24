from data import decimal_guess_df, binary_guess_df, wildcard_df

def save_results():
    """ Function to save results to CSV files """
    decimal_guess_df.to_csv("decimal_guess.csv", index=False)
    binary_guess_df.to_csv("binary_guess.csv", index=False)
    wildcard_df.to_csv("wildcard.csv", index=False)
    print("Results saved to 'decimal_guess.csv', 'binary_guess.csv', and 'wildcard.csv'")
