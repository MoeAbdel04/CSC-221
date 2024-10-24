import pandas as pd

# DataFrames to store results
decimal_guess_df = pd.DataFrame(columns=["Random Binary", "Correct Decimal", "Result"])
binary_guess_df = pd.DataFrame(columns=["Random Decimal", "Correct Binary", "Result"])
wildcard_df = pd.DataFrame(columns=["Question", "Correct Answer", "User Answer", "Result"])
