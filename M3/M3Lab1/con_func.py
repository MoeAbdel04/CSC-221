







from m2Lab_classes import Customer
import csv

def menu():
    # Display the header
    print("=" * 40)
    print("       Customer Management System")
    print("=" * 40)
    print("1. Display Customer Dataset")
    print("2. Add Customer")
    print("3. Update Customer Info")
    print("4. Exit Program and Generate Customer Files")
    print("=" * 40)

def get_cusInfo():
    '''
    Function to read csv file of customers and create Customer Instances
    Returns
    -------
    customers : List of Customer Instances.
    '''
    customers = []

    try:
        with open('customer1.csv', newline='') as customer_file:  
            reader = csv.reader(customer_file)
            next(reader)  # Skip header row

            # Process rows
            for row in reader:
                first, last, phone, email, state, address = row
                customer = Customer(first, last, phone, email, state, address)
                customers.append(customer)

    except FileNotFoundError:
        print("File Error! Customer File Not Found!")

    return customers
