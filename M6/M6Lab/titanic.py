







import pandas as pd

import loop_file as l

df_titanic = pd.read_excel('titanic3.xlsx')


def main():
    
    choice =0
    while choice != 7:
        
        l.menu()
    
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            l.display_dataset(df_titanic)
        elif choice == 2:
            # Using len() function
            num_records = len(df_titanic)
            print(f"Number of records using len(): {num_records}")
            print()
        elif choice == 3:
            
            # Filter rows based on a condition
 
            count = df_titanic[df_titanic['survived'] == 1].shape[0]

            print(f"Number of Survived: {count}")
            
            count = df_titanic[df_titanic['survived'] == 0].shape[0]

            print(f"Number that did not Survive: {count}")
            
        elif choice == 4:
            # Filter rows based on a condition
 
            count = df_titanic[df_titanic['gender'] == 'female'].shape[0]

            print(f"Number of Female passenders: {count}")
            
            count = df_titanic[df_titanic['gender'] == 'male'].shape[0]

            print(f"Number of Male passengers: {count}")
        elif choice ==5:
            #group by port
            # Group by a column and calculate mean(average)
            print('\nNumber of passengers that boarded from each port')
            print(df_titanic.groupby('Port of Embark')['survived'].count())
        elif choice == 6:
            
            print('\nNumber of survived by age group')
            filtered_df = df_titanic[(df_titanic['Age Group'].notna()) & (df_titanic['survived'] == 1) & (df_titanic['survived'].notna())]
            #filtered_df = df_titanic[(df_titanic['survived'] == 1) & (df_titanic['survived'].notna())]
            
            # Apply groupby and count records
            count_per_group = filtered_df.groupby('Age Group').size()


            print(count_per_group)
            
            print('\nNumber that Did not survive by age group')
            filtered_df2 = df_titanic[(df_titanic['Age Group'].notna()) & (df_titanic['survived'] == 0) & (df_titanic['survived'].notna())]
            
            # Apply groupby and count records
            count_per_group2 = filtered_df2.groupby('Age Group').size()
            print(count_per_group2)
        elif choice == 7:
            print("Thank you for using the program.")
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    
    main()