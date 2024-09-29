import con_func as fn
from m2Lab_classes import Customer
import pandas as pd
import csv

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
            if customers:
                print("\nCurrent Customer Dataset:\n")
                print(f'{"First Name":<20}{"Last Name":<20}{"Phone":<20}{"Email":<20}{"Address":<30}{"State":<10}')
                print("-" * 120)
                for cus in customers:
                    print(cus)  # This uses the __repr__ method from Customer class
            else:
                print("No customer data available.")
        
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
            print("Exiting and saving customer data to updated CSV file...")
            # Saving the updated customer list to a new CSV file
            save_to_csv(customers)
            print("Customer data saved successfully.")
        
        else:
            print("Invalid option. Please try again.")

# Function to save customer data to CSV
def save_to_csv(customers):
    # Open a new CSV file for writing the updated data
    with open('updated_customer.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["First Name", "Last Name", "Phone", "Email", "State", "Address"])
        # Write each customer's data
        for cus in customers:
            writer.writerow([cus.get_first(), cus.get_last(), cus.get_phone(), cus.get_email(), cus.get_state(), cus.get_address()])

if __name__ == '__main__':
    main()
