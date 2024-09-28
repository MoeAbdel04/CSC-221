








# Create the subclass Contact
# Initialize new attributes for the class
# Define setters and getters
# Create the menu 
# Set up a try-catch to read the CSV file content and create instances
# Write contact information into a txt file and display contact text file to the user

import con_func as fn
from m2Lab_classes import Customer
import pandas as pd

def main():
    # Call function that reads CSV file and creates instances
    customers = fn.get_cusInfo()  # List references Customer instances

    # Create the main loop which will keep the program running until the user exits
    choice = 0
    while choice != '4':  # Not exit
        # Display menu
        fn.menu()

        choice = input("Please enter an option > ")
        
        if choice == '1':  # Display instances
            # Read instances from list and display 
            for cus in customers:
                print(cus)
        
        elif choice == '2':  # Add customer
            first = input("Enter first name: ")
            last = input("Enter last name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            state = input("Enter state: ")
            address = input("Enter address: ")
            
            new_customer = Customer(first, last, phone, email, state, address)
            customers.append(new_customer)
            print(f"Customer {first} {last} added.")
        
        elif choice == '3':  # Update customer info (simplified for demo)
            print("Update customer feature not implemented.")
        
        elif choice == '4':
            print("Exiting and saving customer data...")
            # You can implement file saving here
            
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
