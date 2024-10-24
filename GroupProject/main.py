from conversion import binary_to_decimal, decimal_to_binary
from subnet_questions import subnet_question
from save_results import save_results

def main_menu():
    """ Main menu for program """
    while True:
        print("\nMenu:")
        print("1. Binary to Decimal Conversion")
        print("2. Decimal to Binary Conversion")
        print("3. Subnet Address Question")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            binary_to_decimal()
        elif choice == "2":
            decimal_to_binary()
        elif choice == "3":
            subnet_question()
        elif choice == "9":
            save_results()
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
