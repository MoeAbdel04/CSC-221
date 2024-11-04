#Database retreival
# 11/1/2024
# CSC221 M5Pro
# Mahamed Abdel







import sqlite3
import pandas as pd

DB_NAME = "vet_serv.db"

def connect_db():
    """
    Establish a connection to the SQLite database.

    Returns:
        connection: A connection object to the SQLite database, or None if there's an error.
    """
    # Pseudocode:
    # TRY to connect to the SQLite database with DB_NAME
    # IF there is an error, PRINT the error message and return None
    # ELSE return the database connection

    try:
        return sqlite3.connect(DB_NAME)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def fetch_all_from_table(table_name):
    """
    Retrieve all records from the specified table.
    
    Args:
        table_name (str): The name of the table to fetch records from.
    
    Returns:
        DataFrame: A DataFrame containing records from the specified table,
                    or an empty DataFrame if an error occurs.
    """
    # Pseudocode:
    # Connect to the database
    # IF connection fails, return an empty DataFrame
    # TRY to execute a SQL query to fetch all records from table_name
    # RETURN the fetched DataFrame
    # CATCH any exceptions and print the error
    # FINALLY, close the database connection

    conn = connect_db()
    if conn is None:
        return pd.DataFrame()

    try:
        query = f"SELECT * FROM {table_name}"  # SQL query to get all records
        df = pd.read_sql_query(query, conn)  # Fetching data into DataFrame
        return df
    except Exception as e:
        print(f"Error fetching data from {table_name}: {e}")
        return pd.DataFrame()
    finally:
        conn.close()  # Close the database connection

def fetch_owner_pet_data(owner_id):
    """
    Retrieve owner and pet data for a specific owner.

    Args:
        owner_id (int): The ID of the owner.

    Returns:
        DataFrame: A DataFrame containing the owner's and their pets' data,
                    or an empty DataFrame if an error occurs.
    """
    # Pseudocode:
    # Connect to the database
    # IF connection fails, return an empty DataFrame
    # TRY to execute a SQL query to get owner and pet data using owner_id
    # RETURN the fetched DataFrame
    # CATCH any exceptions and print the error
    # FINALLY, close the database connection

    conn = connect_db()
    if conn is None:
        return pd.DataFrame()

    try:
        query = """
        SELECT O.OwnerId, O.OwnerFirstName, O.OwnerLastName, 
               O.OwnerPhone, O.OwnerEmail, 
               P.PetId, P.PetName, P.PetBreed, P.PetDOB 
        FROM OWNER O 
        JOIN PETS P ON O.OwnerId = P.OwnerId 
        WHERE O.OwnerId = ?"""
        df = pd.read_sql_query(query, conn, params=(owner_id,))
        return df
    except Exception as e:
        print(f"Error fetching owner pet data: {e}")
        return pd.DataFrame()
    finally:
        conn.close()

def fetch_charge_data_by_owner(owner_id):
    """
    Retrieve charge details for a specific owner.

    Args:
        owner_id (int): The ID of the owner.

    Returns:
        DataFrame: A DataFrame containing the owner's charge data,
                    or an empty DataFrame if an error occurs.
    """
    # Pseudocode:
    # Connect to the database
    # IF connection fails, return an empty DataFrame
    # TRY to execute a SQL query to fetch charge data for the owner using owner_id
    # RETURN the fetched DataFrame
    # CATCH any exceptions and print the error
    # FINALLY, close the database connection

    conn = connect_db()
    if conn is None:
        return pd.DataFrame()

    try:
        query = """
        SELECT O.OwnerId, O.OwnerFirstName, O.OwnerLastName, 
               O.OwnerEmail, P.PetId, P.PetName, 
               P.Service, P.Date, P.Charge 
        FROM OWNER O 
        JOIN PETS P ON O.OwnerId = P.OwnerId 
        WHERE O.OwnerId = ?"""
        df = pd.read_sql_query(query, conn, params=(owner_id,))
        return df
    except Exception as e:
        print(f"Error fetching charge data: {e}")
        return pd.DataFrame()
    finally:
        conn.close()

def fetch_pet_information_by_breed(pet_breed):
    """
    Retrieve pet information by breed.

    Args:
        pet_breed (str): The breed of pets to search for.

    Returns:
        DataFrame: A DataFrame containing pets of the specified breed,
                    or an empty DataFrame if an error occurs.
    """
    # Pseudocode:
    # Connect to the database
    # IF connection fails, return an empty DataFrame
    # TRY to execute a SQL query to fetch pets by pet_breed
    # RETURN the fetched DataFrame
    # CATCH any exceptions and print the error
    # FINALLY, close the database connection

    conn = connect_db()
    if conn is None:
        return pd.DataFrame()

    try:
        query = "SELECT * FROM PETS WHERE PetBreed = ?"  # SQL query to get pets by breed
        df = pd.read_sql_query(query, conn, params=(pet_breed,))
        return df
    except Exception as e:
        print(f"Error fetching pet information: {e}")
        return pd.DataFrame()
    finally:
        conn.close()

def save_to_csv(df, filename):
    """
    Save the DataFrame to a CSV file.

    Args:
        df (DataFrame): The DataFrame to save.
        filename (str): The name of the file to save to.
    """
    # Pseudocode:
    # TRY to save the DataFrame df to the specified filename in CSV format
    # PRINT a success message if save is successful
    # CATCH any exceptions and print the error message

    try:
        df.to_csv(filename, index=False)  # Save DataFrame to CSV
        print(f"Data saved to {filename}.")
    except Exception as e:
        print(f"Error saving DataFrame to CSV: {e}")