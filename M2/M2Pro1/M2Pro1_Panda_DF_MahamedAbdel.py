# Reading files into a dataframe.
# 9/20/24
# CSC221 M2Pro1– Panda DF
# Mahamed Abdel


# main_program.py

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
