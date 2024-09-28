





# -*- coding: utf-8 -*-
from m2Lab_classes import Customer
import csv

def menu():
    # Display the header
    print("Menu")
    print("----------------")
    print("1. Display Customer Dataset"
          + "\\n2. Add Customer"
          + "\\n3. Update Customer Info"
          + "\\n4. Exit Program and Generate Customer Files")

def get_cusInfo():
    '''
    Function to read csv file of customers and create Customer Instances
    Returns
    -------
    customers : List of Customer Instances.
    '''
    customers = []

    try:
        with open('customer(1).csv', newline='') as customer_file:  # Updated file path
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
