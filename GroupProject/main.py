from functions import ask_subnet_question, binary_to_decimal, decimal_to_binary, save_results

def main_menu():
    """
    Main menu to navigate between different questions and conversions.
    """
    exit_program = False  # This flag will control when to exit the loop
    
    while not exit_program:
        print("\nMenu:")
        print("1. Subnet Address Question")
        print("2. Decimal to Binary Conversion")
        print("3. Binary to Decimal Conversion")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            ask_subnet_question()
        elif choice == "2":
            decimal_to_binary()
        elif choice == "3":
            binary_to_decimal()
        elif choice == "4":
            save_results()
            print("Thank you for using the program!")
            exit_program = True  # Set the flag to True to exit the loop
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
