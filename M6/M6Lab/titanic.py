# Graph plot
# 11/15/24
# CSC221 M6Lab
# Mahamed Abdel



import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the file path
file_path = r'C:\Users\PC\Downloads\CSC-221-6\titanic3.xlsx'

# Check if the file exists
if os.path.exists(file_path):
    try:
        # Load the Excel file into a DataFrame
        df_titanic = pd.read_excel(file_path)
        print("Titanic file loaded successfully!")
    except Exception as e:
        print(f"An error occurred while loading the Titanic file: {e}")
else:
    print("File not found. Ensure the path to the Titanic file is correct!")
    exit()

# Main Program Functionality
def plot_and_save(data, x, y, title, xlabel, ylabel, filename):
    """Helper function to create and save plots."""
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x, y=y, data=data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(labels=[ylabel], loc='upper right', bbox_to_anchor=(1.1, 1.05))
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()


def main():
    choice = 0
    while choice != 7:
        menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                display_dataset(df_titanic)
            elif choice == 2:
                num_records = len(df_titanic)
                print(f"Number of records: {num_records}")
                plot_data = pd.DataFrame({'Count': [num_records]}, index=['Total Records']).reset_index()
                plot_and_save(plot_data, 'index', 'Count', 'Total Number of Records', 'Category', 'Count', 'total_records.png')
            elif choice == 3:
                survived_count = df_titanic['survived'].value_counts().reset_index()
                survived_count.columns = ['Survived', 'Count']
                print(survived_count)
                plot_and_save(survived_count, 'Survived', 'Count', 'Survival Count', 'Survived (0 = No, 1 = Yes)', 'Count', 'survival_count.png')
            elif choice == 4:
                gender_count = df_titanic['gender'].value_counts().reset_index()
                gender_count.columns = ['Gender', 'Count']
                print(gender_count)
                plot_and_save(gender_count, 'Gender', 'Count', 'Gender Distribution', 'Gender', 'Count', 'gender_count.png')
            elif choice == 5:
                port_count = df_titanic['Port of Embark'].value_counts().reset_index()
                port_count.columns = ['Port', 'Count']
                print(port_count)
                plot_and_save(port_count, 'Port', 'Count', 'Passengers by Port of Embarkation', 'Port', 'Count', 'port_count.png')
            elif choice == 6:
                age_survived = df_titanic[df_titanic['survived'] == 1]['Age Group'].value_counts().reset_index()
                age_survived.columns = ['Age Group', 'Survived Count']
                age_not_survived = df_titanic[df_titanic['survived'] == 0]['Age Group'].value_counts().reset_index()
                age_not_survived.columns = ['Age Group', 'Not Survived Count']
                print("Survived by Age Group:")
                print(age_survived)
                print("Did Not Survive by Age Group:")
                print(age_not_survived)
                combined = pd.merge(age_survived, age_not_survived, on='Age Group', how='outer').fillna(0)
                combined_melted = combined.melt(id_vars='Age Group', value_vars=['Survived Count', 'Not Survived Count'], 
                                                var_name='Category', value_name='Count')
                sns.set(style="whitegrid")
                plt.figure(figsize=(12, 8))
                sns.barplot(x='Age Group', y='Count', hue='Category', data=combined_melted)
                plt.title('Survival by Age Group')
                plt.xlabel('Age Group')
                plt.ylabel('Count')
                plt.legend(title='Category')
                plt.tight_layout()
                plt.savefig('age_group_survival.png')
                plt.show()
            elif choice == 7:
                print("Thank you for using the program.")
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"Error: {e}")


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
    except Exception as e:
        print(f"Error displaying dataset: {e}")


if __name__ == "__main__":
    main()




    