import pandas as pd
import json


def ADD(Current_table):
    print("Executing command : ADD")
    
    if not Current_table:
        print("Error: No table opened.")
        return

    df = pd.read_csv(f'{Current_table}.csv')
    
    df.reset_index(drop=True, inplace=True)
    columns = list(df.columns)

    
    with open(f"{Current_table}.meta.json", "r") as f:
        data = json.load(f)
        
    primary = data["primary_key"]

    row_data = {}

    for column in columns:
        
        #Prevents duplicate values in primary key column.
        if column == primary:
            while True:
                value = input(f"Value for {column} (PRIMARY KEY): ")
                
                
                if value in df[primary].astype(str).values:
                    print(f"Primary key must be unique. '{value}' already exists.")
                else:
                    row_data[column] = value
                    break
        else:
            value = input(f"Value for {column}: ")
            row_data[column] = value

    
    row_df = pd.DataFrame([row_data])
    row_df.to_csv(f'{Current_table}.csv', mode='a', index=False, header=False)

    print("Row inserted successfully.\n")
    return Current_table



def ADDCOL(Current_table) :
    print("Executing command : ADDCOL ")

    df = pd.read_csv(f"{Current_table}.csv")

    col_name = input("Enter new column name: ").strip()
    default_val = input("Default value: ")

    df[col_name] = default_val
    df.to_csv(f"{Current_table}.csv", index=False)

    return Current_table

def UPDATE(Current_table):
    
    print("Executing command : UPDATE ")

    df = pd.read_csv(f"{Current_table}.csv")

    row_to_update = int(input("Index of row :").strip())

    df.loc[row_to_update] = [input(f"Value of {column}") for column in df.columns]

def UPDATECOL(Current_table):
    
    print("Executing command : UPDATECOL ")

    df = pd.read_csv(f"{Current_table}.csv")

    col_to_update = input("Name of Column").strip()

    condition = int(input("new default value (1) of new list of values").strip())

    if (condition):
        #true
        default_val = input("Default value: ")

        df[col_to_update] = default_val
        df.to_csv(f"{Current_table}.csv", index=False)

    else :
        values = []
        for index in df.index :
            value = input(f"value for row index {index} :")
            values.append(value)

        df[col_to_update] = values
        df.to_csv(f"{Current_table}.csv", index=False)

    return Current_table
