




def menu():
    
    print("\nMenu:")
    print("1. Display dataset")
    print("2. Get Number of record in dataset")
    print("3. Get Num of Survived and Num of Dead")
    print("4. Get number of Females and/or Males")
    print("5. Get number of passengers Boarded from each port")
    print("6. Get number of Survived vs Didn't Survive by age group")
    print("7. Exit")
    print()



def display_dataset(df):
    try:
       print(df.head(15))
    except FileNotFoundError:
        print("File not found!")