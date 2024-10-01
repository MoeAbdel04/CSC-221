# Contacts - Debugging
# 9/27/24
# CSC221 M3Lab1
# Mahamed Abdel





import con_func as fn
from m2Lab_classes import Customer
import pandas as pd
import csv
import os

# Load the base CSV data into customers list
def load_customers_from_csv():
    customers = []
    csv_file = 'customer1.csv'  # Default file name

    # Check if the file exists
    if not os.path.exists(csv_file):
        print(f"Error: The file '{csv_file}' was not found in the current directory.")
        exit()  # Exit the program if the file is not found

    try:
        # Read CSV file and create Customer instances
        df = pd.read_csv(csv_file)
        for _, row in df.iterrows():
            customer = Customer(row['first'], row['last'], row['phone'], row['email'], row['state'], row['address'])
            customers.append(customer)
        return customers
    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' was not found.")
        exit()

# Save updated customers to a new CSV file
def save_to_csv(customers):
    # Open a new CSV file for writing the updated data
    with open('updated_customer.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["First Name", "Last Name", "Phone", "Email", "State", "Address"])
        # Write each customer's data
        for cus in customers:
            writer.writerow([cus.get_first(), cus.get_last(), cus.get_phone(), cus.get_email(), cus.get_state(), cus.get_address()])

# Function to update customer info
def update_customer_info(customers):
    first_name = input("Enter the first name of the customer to update: ")
    last_name = input("Enter the last name of the customer to update: ")
    
    # Search for the customer in the list
    for customer in customers:
        if customer.get_first() == first_name and customer.get_last() == last_name:
            print("Customer found.")
            print(f'{"First Name":<20}{"Last Name":<20}{"Phone":<20}{"Email":<30}{"Address":<30}{"State":<10}')
            print(f'{customer.get_first():<20}{customer.get_last():<20}{customer.get_phone():<20}{customer.get_email():<30}{customer.get_address():<30}{customer.get_state():<10}')
            
            # Allow user to update fields
            update_field = input("Which field would you like to update (phone, email, address, state)? ").lower()

            if update_field == "phone":
                new_phone = input("Enter the new phone number: ")
                customer.set_phone(new_phone)
            elif update_field == "email":
                new_email = input("Enter the new email address: ")
                customer.set_email(new_email)
            elif update_field == "address":
                new_address = input("Enter the new address: ")
                customer.set_address(new_address)
            elif update_field == "state":
                new_state = input("Enter the new state: ")
                customer.set_state(new_state)
            else:
                print("Invalid field selected.")
            print("Customer information updated.")
            return
    print("Customer not found.")

def main():
    # Load customers from the base CSV file
    customers = load_customers_from_csv()

    # Create the main loop which will keep the program running until the user exits
    choice = 0
    while choice != '4':  # Not exit
        # Display menu
        fn.menu()

        choice = input("Please enter an option > ")
        
        if choice == '1':  # Display instances
            if customers:
                print("\nCurrent Customer Dataset:\n")
                print(f'{"First Name":<20}{"Last Name":<20}{"Phone":<20}{"Email":<30}{"Address":<30}{"State":<10}')
                print("-" * 130)
                for cus in customers:
                    print(f'{cus.get_first():<20}{cus.get_last():<20}{cus.get_phone():<20}{cus.get_email():<30}{cus.get_address():<30}{cus.get_state():<10}')
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
        
        elif choice == '3':  # Update customer info
            update_customer_info(customers)
        
        elif choice == '4':
            print("Exiting and saving customer data to updated CSV file...")
            # Saving the updated customer list to a new CSV file
            save_to_csv(customers)
            print("Customer data saved successfully.")
        
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
