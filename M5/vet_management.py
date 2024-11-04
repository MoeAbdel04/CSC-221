
import os
from db_operations import (
    fetch_all_from_table,
    fetch_owner_pet_data,
    fetch_charge_data_by_owner,
    fetch_pet_information_by_breed,
    save_to_csv,
)

def create_directory_if_not_exists(directory):
    """
    Create a directory if it does not already exist.

    Args:
        directory (str): The path of the directory to create.

    Pseudocode:
    If the directory does not exist, create it.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def display_data(df):
    """
    Display the DataFrame in a readable format.

    Args:
        df (DataFrame): The DataFrame to display.
    
    Pseudocode:
    If DataFrame is empty, print "No data to display."
    Else, print the DataFrame.
    """
    if df.empty:
        print("No data to display.")
    else:
        print(df)

def display_owner_content():
    """
    Display all records from the OWNER table and save to a CSV file.

    Pseudocode:
    Fetch all records from the OWNER table.
    Call display_data to show records.
    Save the records to 'example_data/owner.csv'.
    """
    create_directory_if_not_exists("example_data")  # Ensure the directory exists
    df = fetch_all_from_table("OWNER")
    display_data(df)
    save_to_csv(df, "example_data/owner.csv")

def display_pets_content():
    """
    Display all records from the PETS table and save to a CSV file.

    Pseudocode:
    Fetch all records from the PETS table.
    Call display_data to show records.
    Save the records to 'example_data/pets.csv'.
    """
    create_directory_if_not_exists("example_data")  # Ensure the directory exists
    df = fetch_all_from_table("PETS")
    display_data(df)
    save_to_csv(df, "example_data/pets.csv")

def calculate_total_charge_by_owner(owner_id):
    """
    Calculate total charges for a specific owner.

    Args:
        owner_id (int): The ID of the owner.
    
    Returns:
        total_charge (float): Total charge amount for the specified owner.

    Pseudocode:
    Fetch charge data for the owner.
    If data is empty, print a message and return 0.
    Calculate total charge by summing the 'Charge' column.
    Print the DataFrame and total charge.
    Return total charge.
    """
    df = fetch_charge_data_by_owner(owner_id)
    if df.empty:
        print(f"No records found for OwnerId {owner_id}.")
        return 0.0

    total_charge = df["Charge"].sum()
    print(df)
    print(f"Total Charge for OwnerId {owner_id}: ${total_charge:.2f}")
    return total_charge

def retrieve_owner_pet_data(owner_id):
    """
    Retrieve owner and pet data for a specific owner and save to a CSV file.

    Args:
        owner_id (int): The ID of the owner.

    Pseudocode:
    Fetch owner and pet data for the given owner ID.
    If data is empty, print a message.
    Else, display the data and save it to a CSV file using owner's last name.
    """
    create_directory_if_not_exists("example_data")  # Ensure the directory exists
    df = fetch_owner_pet_data(owner_id)
    if df.empty:
        print(f"No records found for OwnerId {owner_id}.")
    else:
        display_data(df)
        owner_last_name = df.iloc[0]["OwnerLastName"].lower()
        output_file = f"example_data/{owner_last_name}_{owner_id}.csv"
        save_to_csv(df, output_file)

def retrieve_pet_information_by_breed(pet_breed):
    """
    Retrieve and display information about pets of a specific breed.

    Args:
        pet_breed (str): The breed of pets to search for.

    Pseudocode:
    Fetch pet information for the specified breed.
    If data is empty, print a message.
    Else, display the data.
    Calculate total and average charge for this breed if the 'Charge' column exists.
    Print the total and average charge.
    """
    df = fetch_pet_information_by_breed(pet_breed)
    if df.empty:
        print(f"No records found for PetBreed '{pet_breed}'.")
    else:
        display_data(df)
        total_charge = df["Charge"].sum() if "Charge" in df else 0.0
        average_charge = df["Charge"].mean() if "Charge" in df else 0.0
        print(f"Total Charges for PetBreed '{pet_breed}': ${total_charge:.2f}")
        print(f"Average Charge for PetBreed '{pet_breed}': ${average_charge:.2f}")

def display_menu():
    """
    Display the main menu options for the user.

    Pseudocode:
    Print menu options.
    """
    print("\nMenu:")
    print("1) Display OWNER content and create DataFrame")
    print("2) Display PETS content and create DataFrame")
    print("3) Retrieve Owner and Pet data for specific Owner")
    print("4) Calculate Total Charge by Owner")
    print("5) Retrieve Pet information by PetBreed")
    print("6) Exit")

def main():
    """
    Main function to run the veterinary management program.

    Pseudocode:
    Initialize a running flag as True.
    While running is True:
        Display menu.
        Get user choice.
        Use if-elif statements to call the corresponding function based on user choice.
        If the choice is '6', set running to False to exit the loop.
    """
    is_running = True
    while is_running:
        display_menu()
        choice = input("Select an option: ")
        
        try:
            if choice == "1":
                display_owner_content()
            elif choice == "2":
                display_pets_content()
            elif choice == "3":
                owner_id = int(input("Enter OwnerId: "))
                retrieve_owner_pet_data(owner_id)
            elif choice == "4":
                owner_id = int(input("Enter OwnerId: "))
                calculate_total_charge_by_owner(owner_id)
            elif choice == "5":
                pet_breed = input("Enter PetBreed: ")
                retrieve_pet_information_by_breed(pet_breed)
            elif choice == "6":
                print("Program will terminate.")
                is_running = False
            else:
                print("Invalid option. Please select again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()    