

import os
import pandas as pd

# Data Handling Functions
def load_data():
    """Load and preprocess the Titanic dataset."""
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Ensures it runs relative to the script location
    
    # Define the path to the Excel file in the same directory as the script
    file_path = os.path.join(script_dir, 'titanic3(1).xlsx')
    
    # Load the Titanic dataset from the Excel file
    df = pd.read_excel(file_path)
    
    # Preprocess the 'Age Group' column
    df = df.dropna(subset=['Age Group']).copy()  # Ensure we're working on a copy of the DataFrame
    df.loc[:, 'Age Group'] = df['Age Group'].str.strip().str.lower().str.title()
    
    return df

# Other functions (menu, operations) go here...


# Menu Functions
def display_menu():
    """Displays the menu options to the user"""
    print("\n--- Titanic Dataset Menu ---")
    print("1. Display dataset")
    print("2. Get Number of records (passengers) listed in dataset")
    print("3. Get number of Survived vs Dead")
    print("4. Get number of Females and/or Males")
    print("5. Get number of passengers Boarded from each port")
    print("6. Get number of Survived vs Didn't Survive by age group")
    print("7. Exit")

def get_user_choice():
    """Prompts the user for a menu choice and returns it"""
    try:
        choice = int(input("\nEnter your choice: "))
        return choice
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

# Operations Functions
def display_dataset(df):
    """Displays the first 15 rows of the dataset"""
    print("\nFirst 15 rows of the dataset:")
    print(df.head(15))

def get_record_count(df):
    """Displays the number of records in the dataset (excluding header)"""
    print(f"\nNumber of records (passengers): {len(df)}")

def get_survived_vs_dead(df):
    """Displays the count of Survived vs Dead passengers"""
    survived_count = df['survived'].value_counts()
    print(f"\nSurvived: {survived_count.get(1, 0)}, Didn't survive: {survived_count.get(0, 0)}")

def get_gender_survival(df):
    """Displays survival counts based on gender"""
    gender_choice = input("Choose one (Females Survived, Males Survived, Both): ").strip().lower().capitalize()
    if gender_choice == 'Females survived':
        survived_females = df[(df['gender'] == 'female') & (df['survived'] == 1)]
        print(f"\nFemales survived: {len(survived_females)}")
    elif gender_choice == 'Males survived':
        survived_males = df[(df['gender'] == 'male') & (df['survived'] == 1)]
        print(f"\nMales survived: {len(survived_males)}")
    elif gender_choice == 'Both':
        survived_females = df[(df['gender'] == 'female') & (df['survived'] == 1)]
        survived_males = df[(df['gender'] == 'male') & (df['survived'] == 1)]
        print(f"\nFemales survived: {len(survived_females)}, Males survived: {len(survived_males)}")
    else:
        print("Invalid choice. Please try again.")
        get_gender_survival(df)

def get_boarding_ports(df):
    """Displays the number of passengers who boarded from each port"""
    port_counts = df['Port of Embark'].value_counts()
    print("\nNumber of passengers boarded from each port:")
    print(port_counts)

def get_age_group_survival(df):
    """Displays survival counts based on age group"""
    age_groups = df['Age Group'].unique()
    print("\nAvailable age groups:", ", ".join(age_groups))
    
    age_group_choice = input("Enter an age group from the list: ").strip().lower().title()

    if age_group_choice in age_groups:
        age_group_data = df[df['Age Group'] == age_group_choice]
        survived_count = age_group_data['survived'].value_counts()
        total_in_group = len(age_group_data)
        survived = survived_count.get(1, 0)
        not_survived = survived_count.get(0, 0)
        survival_rate = (survived / total_in_group) * 100 if total_in_group > 0 else 0
        print(f"\nIn age group '{age_group_choice}':")
        print(f"Survived: {survived}, Didn't survive: {not_survived}")
        print(f"Survival rate: {survival_rate:.2f}%")
    else:
        print("Invalid age group. Please try again.")
        get_age_group_survival(df)
