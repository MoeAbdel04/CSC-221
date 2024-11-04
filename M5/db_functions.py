import sqlite3
import pandas as pd

def connect_db(db_name="vet_serv.db"):
    return sqlite3.connect(db_name)

def get_dataframe(query, db_connection):
    return pd.read_sql_query(query, db_connection)

def save_to_csv(df, filename):
    df.to_csv(filename, index=False)

def display_owner_data(db_connection):
    query = "SELECT * FROM OWNER"
    df = get_dataframe(query, db_connection)
    save_to_csv(df, "owner.csv")
    return df

def display_pets_data(db_connection):
    query = "SELECT * FROM PETS"
    df = get_dataframe(query, db_connection)
    save_to_csv(df, "pets.csv")
    return df

def retrieve_owner_pet_data(db_connection, owner_id):
    query = f"""
    SELECT OWNER.OwnerId, OWNER.OwnerFirstName, OWNER.OwnerLastName, OWNER.OwnerPhone, OWNER.OwnerEmail,
           PETS.PetId, PETS.PetName, PETS.PetBreed, PETS.PetDOB
    FROM OWNER
    JOIN PETS ON OWNER.OwnerId = PETS.OwnerId
    WHERE OWNER.OwnerId = {owner_id}
    """
    df = get_dataframe(query, db_connection)
    if not df.empty:
        last_name = df['OwnerLastName'].iloc[0].lower()
        filename = f"{last_name}_{owner_id}.csv"
        save_to_csv(df, filename)
    return df

def calculate_total_charge(db_connection, owner_id):
    query = f"""
    SELECT OWNER.OwnerId, OWNER.OwnerFirstName, OWNER.OwnerLastName, OWNER.OwnerEmail,
           PETS.PetId, PETS.PetName, PETS.PetBreed, PETS.Service, PETS.Date, PETS.Charge
    FROM OWNER
    JOIN PETS ON OWNER.OwnerId = PETS.OwnerId
    WHERE OWNER.OwnerId = {owner_id}
    """
    df = get_dataframe(query, db_connection)
    total_charge = df['Charge'].sum() if not df.empty else 0
    return df, total_charge

def retrieve_pet_by_breed(db_connection, breed):
    query = f"SELECT * FROM PETS WHERE PetBreed = '{breed}'"
    df = get_dataframe(query, db_connection)
    total_charges = df['Charge'].sum() if not df.empty else 0
    average_charge = df['Charge'].mean() if not df.empty else 0
    return df, total_charges, average_charge
