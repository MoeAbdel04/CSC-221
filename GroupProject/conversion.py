import random
from data import binary_guess_df, decimal_guess_df
import pandas as pd

def binary_to_decimal():
    """ Binary to Decimal conversion game """
    random_decimal = random.randint(0, 255)
    random_binary = format(random_decimal, '08b')
    print(f"\nRandom Binary: {random_binary}")
    
    user_guess = input("Enter the Decimal value of the binary number: ")
    
    if int(user_guess) == random_decimal:
        print("Correct! The binary was indeed", random_binary)
        result = "Correct"
    else:
        print(f"Wrong! The correct decimal value was {random_decimal}")
        result = "Wrong"
    
    # Add to DataFrame and print the updated DataFrame
    new_row = pd.DataFrame([{
        "Random Binary": random_binary, 
        "Correct Decimal": random_decimal, 
        "Result": result
    }])
    
    global decimal_guess_df
    decimal_guess_df = pd.concat([decimal_guess_df, new_row], ignore_index=True)
    
    # Print the DataFrame after the update
    print("\nUpdated decimal_guess_df:")
    print(decimal_guess_df)

    # Submenu
    print("\n1) Reset (generate another random binary)")
    print("2) Back to main menu")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        binary_to_decimal()

def decimal_to_binary():
    """ Decimal to Binary conversion game """
    random_decimal = random.randint(0, 255)
    correct_binary = format(random_decimal, '08b')
    print(f"\nRandom Decimal: {random_decimal}")
    
    user_guess = input("Enter the Binary value of the decimal number: ")
    
    if user_guess == correct_binary:
        print("Correct! The decimal was indeed", random_decimal)
        result = "Correct"
    else:
        print(f"Wrong! The correct binary value was {correct_binary}")
        result = "Wrong"
    
    # Add to DataFrame and print the updated DataFrame
    new_row = pd.DataFrame([{
        "Random Decimal": random_decimal, 
        "Correct Binary": correct_binary, 
        "Result": result
    }])
    
    global binary_guess_df
    binary_guess_df = pd.concat([binary_guess_df, new_row], ignore_index=True)
    
    # Print the DataFrame after the update
    print("\nUpdated binary_guess_df:")
    print(binary_guess_df)

    # Submenu
    print("\n1) Reset (generate another random decimal)")
    print("2) Back to main menu")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        decimal_to_binary()
