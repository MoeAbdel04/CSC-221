import db_functions as dbf

def main_menu():
    print("\nMenu:")
    print("1) Display OWNER content and create DataFrame")
    print("2) Display PETS content and create DataFrame")
    print("3) Retrieve Owner and Pet data for specific Owner")
    print("4) Calculate Total Charge by Owner")
    print("5) Retrieve Pet information by PetBreed")
    print("6) Exit")

def main():
    db_connection = dbf.connect_db()
    
    while True:
        main_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                df = dbf.display_owner_data(db_connection)
                print(df)
            elif choice == 2:
                df = dbf.display_pets_data(db_connection)
                print(df)
            elif choice == 3:
                owner_id = int(input("Enter OwnerId: "))
                df = dbf.retrieve_owner_pet_data(db_connection, owner_id)
                print(df if not df.empty else "No data found for the specified OwnerId.")
            elif choice == 4:
                owner_id = int(input("Enter OwnerId: "))
                df, total_charge = dbf.calculate_total_charge(db_connection, owner_id)
                print(df if not df.empty else "No data found for the specified OwnerId.")
                print(f"Total charge for owner: {total_charge}")
            elif choice == 5:
                breed = input("Enter PetBreed: ")
                df, total_charges, average_charge = dbf.retrieve_pet_by_breed(db_connection, breed)
                print(df if not df.empty else "No data found for the specified breed.")
                print(f"Total charges for {breed}: {total_charges}, Average charge: {average_charge}")
            elif choice == 6:
                print("Program will terminate.")
                break
            else:
                print("Invalid option. Please select again.")
        except Exception as e:
            print(f"Error: {e}. Please enter a valid choice.")
    db_connection.close()

if __name__ == "__main__":
    main()
