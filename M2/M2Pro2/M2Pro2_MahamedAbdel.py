# Binary/Decimal conversion
# 9/20/24
# CSC221 M2Pro2
# Mahamed Abdel



import random
import pandas as pd

# DataFrames to store results
decimal_guess_df = pd.DataFrame(columns=["Random Binary", "Correct Decimal", "Result"])
binary_guess_df = pd.DataFrame(columns=["Random Decimal", "Correct Binary", "Result"])

def binary_to_decimal():
    """
    Function to handle Binary to Decimal conversion game.
    Generates a random binary number and asks the user to guess its decimal value.
    """
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
    
    # Add to DataFrame
    global decimal_guess_df
    decimal_guess_df = pd.concat([decimal_guess_df, pd.DataFrame([{
        "Random Binary": random_binary, 
        "Correct Decimal": random_decimal, 
        "Result": result
    }])], ignore_index=True)

    # Submenu
    print("\n1) Reset (generate another random binary)")
    print("2) Back to main menu")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        binary_to_decimal()
    elif choice == "2":
        return

def decimal_to_binary():
    """
    Function to handle Decimal to Binary conversion game.
    Generates a random decimal number and asks the user to guess its binary value.
    """
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
    
    # Add to DataFrame
    global binary_guess_df
    binary_guess_df = pd.concat([binary_guess_df, pd.DataFrame([{
        "Random Decimal": random_decimal, 
        "Correct Binary": correct_binary, 
        "Result": result
    }])], ignore_index=True)

    # Submenu
    print("\n1) Reset (generate another random decimal)")
    print("2) Back to main menu")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        decimal_to_binary()
    elif choice == "2":
        return

def save_results():
    """
    Function to save both DataFrames (binary_guess and decimal_guess) to CSV files.
    """
    decimal_guess_df.to_csv("decimal_guess.csv", index=False)
    binary_guess_df.to_csv("binary_guess.csv", index=False)
    print("Results saved to 'decimal_guess.csv' and 'binary_guess.csv'")

def main_menu():
    """
    Main menu to navigate between different conversion functions.
    """
    while True:
        print("\nMenu:")
        print("1. Binary to Decimal Conversion")
        print("2. Decimal to Binary Conversion")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            binary_to_decimal()
        elif choice == "2":
            decimal_to_binary()
        elif choice == "9":
            save_results()
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

