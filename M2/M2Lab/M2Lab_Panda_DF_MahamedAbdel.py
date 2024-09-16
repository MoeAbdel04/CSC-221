# Contacts using Dataframes
# 9/12/24
# CSC221 M2Lab– Panda DF
# Mahamed Abdel



import pandas as pd

# Custom function to display section titles
def display_title(title):
    print(f"\n--- {title} ---\n")

# Custom function to load CSV data
def load_data():
    try:
        # Sample data for contacts.csv
        contacts_data = {
            'email': ['dhsmith@yahoo.com', 'smsmith@yahoo.com', 'tessbijon@gmail.com'],
            'first': ['Dan', 'Susan', 'Tess'],
            'last': ['Smith', 'Smith', 'Bijon'],
            'phone': ['801-555-1223', '914-555-4455', None]
        }

        # Sample data for contact-states.csv
        contact_states_data = {
            'email': ['dhsmith@yahoo.com', 'stefsmith@gmail.com'],
            'state': ['NY', 'NJ']
        }

        # Create DataFrames
        contacts_df = pd.DataFrame(contacts_data)
        contact_states_df = pd.DataFrame(contact_states_data)

        return contacts_df, contact_states_df

    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None

# Main function to perform all the tasks
def main():
    contacts_df, contact_states_df = load_data()

    if contacts_df is None or contact_states_df is None:
        print("Failed to load data.")
        return

    # a) Display loaded data
    display_title("a) Loaded Data")
    print(contacts_df)

    # b) Use info() method to determine non-null values and column types
    display_title("b) Info Method Output")
    print(contacts_df.info())

    # c) Number of rows and columns
    display_title("c) Number of Rows and Columns")
    print(f"Rows: {len(contacts_df)}")
    print(f"Columns: {len(contacts_df.columns)}")

    # d) Display the first two and last two rows using head() and tail()
    display_title("d) First Two and Last Two Rows")
    print(contacts_df.head(2))
    print(contacts_df.tail(2))

    # e) Display the phone column
    display_title("e) Phone Column")
    print(contacts_df['phone'])

    # f) Display columns named first and last
    display_title("f) First and Last Columns")
    print(contacts_df[['first', 'last']])

    # g) Display the phone number for the row with email = 'smsmith@yahoo.com'
    display_title("g) Phone number for smsmith@yahoo.com")
    print(contacts_df.loc[contacts_df['email'] == 'smsmith@yahoo.com', 'phone'])

    # h) Display the data sorted by last name then first name
    display_title("h) Sorted by Last Name, then First Name")
    print(contacts_df.sort_values(by=['last', 'first']))

    # i) Display rows where the first name is Dan
    display_title("i) Rows where first name is Dan")
    print(contacts_df[contacts_df['first'] == 'Dan'])

    # j) Display rows where the phone number is missing
    display_title("j) Rows where phone number is missing")
    print(contacts_df[contacts_df['phone'].isnull()])

    # k) Update phone for tessbijon@gmail.com
    display_title("k) Updating Phone for tessbijon@gmail.com")
    contacts_df.loc[contacts_df['email'] == 'tessbijon@gmail.com', 'phone'] = '555-1233'
    print(contacts_df)

    # l) Drop row where email = 'tessbijon@gmail.com'
    display_title("l) Dropping row for tessbijon@gmail.com")
    contacts_df = contacts_df[contacts_df['email'] != 'tessbijon@gmail.com']
    print(contacts_df)

    # m) Append a new row for stefsmith@gmail.com
    display_title("m) Appending new row (stefsmith@gmail.com)")
    new_row = pd.DataFrame([{'email': 'stefsmith@gmail.com', 'first': 'Stef', 'last': 'Smith', 'phone': '801-555-9876'}])
    contacts_df = pd.concat([contacts_df, new_row], ignore_index=True)
    print(contacts_df)

    # n) Join contact-states.csv to the contacts DataFrame using the email field
    display_title("n) Joining contact-states data")
    merged_df = pd.merge(contacts_df, contact_states_df, on='email', how='left')
    print(merged_df)

    # Save the updated DataFrame to a CSV file in the current directory
    output_file = 'updated_contacts_with_tess.csv'
    merged_df.to_csv(output_file, index=False)
    print(f"\nFinal merged DataFrame saved to {output_file}")

# Run the main function
main()
