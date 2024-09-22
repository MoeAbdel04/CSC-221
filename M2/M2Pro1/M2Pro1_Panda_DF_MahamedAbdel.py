# Reading files into a dataframe.
# 9/20/24
# CSC221 M2Pro1– Panda DF
# Mahamed Abdel


"""""
Pseudocode for Titanic Menu-Driven Program

1. **Program Structure Overview**:
    - The program is split into two files:
        a. M2Pro1_Func.py`  Contains all the data handling, menu, and operations functions.
        b. M2Pro1_Panda_DF_MahamedAbdel.py`  The main script that orchestrates the menu and calls functions.
    - The Excel file containing the Titanic dataset is expected to be in the same directory as the Python files.

2. **Main Program Flow (main_program.py)**:
    a. Import necessary functions 
    b. Define the main function:
        - Call `load_data()` to load and preprocess the Titanic dataset.
        - Initialize a loop that continues until the user selects the "Exit" option from the menu.
        - Within the loop:
            i. Display the menu using `display_menu()`.
            ii. Get the user's choice using `get_user_choice()`.
            iii. Based on the user's choice, call the appropriate function:
                - 1: Display the dataset.
                - 2: Get the number of records (passengers) in the dataset.
                - 3: Get the number of survived vs. dead passengers.
                - 4: Get the number of male/female passengers who survived.
                - 5: Get the number of passengers boarded from each port.
                - 6: Get survival data by age group.
                - 7: Exit the program.
            iv. If the user input is invalid, prompt the user to enter a valid choice.
        - End the loop and display a farewell message when the user chooses to exit.

3. **Functions File**:
    a. **Data Handling**:
        - `load_data()`: 
            i. Load the Titanic dataset from the Excel file.
            ii. Preprocess the dataset by cleaning up the "Age Group" column (remove extra spaces and standardize capitalization).
            iii. Return the processed DataFrame.
    
    b. **Menu Handling**:
        - `display_menu()`: Display the available options for the user to choose from.
        - `get_user_choice()`: Get the user's input and handle invalid inputs by returning `None` if an invalid choice is made.
    
    c. **Operations**:
        - `display_dataset(df)`: Display the first 15 rows of the Titanic dataset.
        - `get_record_count(df)`: Display the total number of passenger records (excluding the header row).
        - `get_survived_vs_dead(df)`: Calculate and display the number of passengers who survived vs those who did not.
        - `get_gender_survival(df)`: Ask the user to choose between females, males, or both and display survival statistics accordingly.
        - `get_boarding_ports(df)`: Display the number of passengers who boarded from each port.
        - `get_age_group_survival(df)`: 
            i. Ask the user to select an age group from the available options.
            ii. Filter the dataset based on the chosen age group.
            iii. Display the survival statistics for the selected age group (including survival rate).
"""


# Import functions from the titanic_functions.py file
from M2Pro1_Func import load_data, display_menu, get_user_choice
from M2Pro1_Func import display_dataset, get_record_count, get_survived_vs_dead
from M2Pro1_Func import get_gender_survival, get_boarding_ports, get_age_group_survival

def main():
    """Main function to run the menu-driven program"""
    df = load_data()  # Load and preprocess data

    exit_program = False
    
    while not exit_program:
        display_menu()  # Display menu options
        choice = get_user_choice()  # Get user choice
        
        if choice == 1:
            display_dataset(df)
        elif choice == 2:
            get_record_count(df)
        elif choice == 3:
            get_survived_vs_dead(df)
        elif choice == 4:
            get_gender_survival(df)
        elif choice == 5:
            get_boarding_ports(df)
        elif choice == 6:
            get_age_group_survival(df)
        elif choice == 7:
            print("Thank you for using the program!")
            exit_program = True
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == '__main__':
    main()
