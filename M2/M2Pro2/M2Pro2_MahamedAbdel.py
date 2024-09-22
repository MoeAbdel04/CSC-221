# Binary/Decimal conversion
# 9/20/24
# CSC221 M2Pro2
# Mahamed Abdel




# Pseudocode for the Binary-Decimal Conversion Program

# Import necessary libraries
# - random: For generating random numbers
# - pandas: For managing data and storing guesses in DataFrames

# Initialize two empty DataFrames to store results:
# - decimal_guess_df: For storing results of the binary-to-decimal guesses
# - binary_guess_df: For storing results of the decimal-to-binary guesses

# Function: binary_to_decimal()
#     1. Generate a random decimal number between 0 and 255
#     2. Convert the random decimal number to an 8-bit binary string
#     3. Display the generated binary number
#     4. Ask the user to guess the corresponding decimal value
#     5. Check if the user's guess is correct:
#         - If correct, display a success message
#         - If wrong, display the correct answer
#     6. Store the generated binary, correct decimal value, and the result (Correct/Wrong) in decimal_guess_df
#     7. Display a submenu:
#         - Option 1: Reset the game (generate another random binary number)
#         - Option 2: Return to the main menu

# Function: decimal_to_binary()
#     1. Generate a random decimal number between 0 and 255
#     2. Convert the random decimal number to an 8-bit binary string
#     3. Display the generated decimal number
#     4. Ask the user to guess the corresponding binary value
#     5. Check if the user's guess is correct:
#         - If correct, display a success message
#         - If wrong, display the correct answer
#     6. Store the generated decimal, correct binary value, and the result (Correct/Wrong) in binary_guess_df
#     7. Display a submenu:
#         - Option 1: Reset the game (generate another random decimal number)
#         - Option 2: Return to the main menu

# Function: save_results()
#     1. Write the decimal_guess_df DataFrame to a CSV file named 'decimal_guess.csv'
#     2. Write the binary_guess_df DataFrame to a CSV file named 'binary_guess.csv'
#     3. Notify the user that the results have been saved

# Function: main_menu()
#     1. Display the main menu with the following options:
#         - Option 1: Binary to Decimal Conversion
#         - Option 2: Decimal to Binary Conversion
#         - Option 9: Exit the program
#     2. Based on the user's choice, call the corresponding function:
#         - If the user chooses Option 1, call binary_to_decimal()
#         - If the user chooses Option 2, call decimal_to_binary()
#         - If the user chooses Option 9, call save_results() and exit the program
#     3. If the user makes an invalid choice, notify them and display the menu again

# Main Program Execution:
#     - Call main_menu() to start the program






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

