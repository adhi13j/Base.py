import pandas as pd
import os

def DEL (Current_table) :
    print("Executing command : DEL")
    
    if not Current_table:
        print("Error: No table opened.")
        return

    df = pd.read_csv(f"{Current_table}.csv")

    try :
        index_to_delete = int(input("Index to delete : "))
    except ValueError:
        print("Invalid index.")
        return
    
    if index_to_delete < 0 or index_to_delete >= len(df):
        print("Index out of range.")
        return

    df = df.drop(index_to_delete).reset_index(drop=True)
    df.to_csv(f"{Current_table}.csv", index=True)

    return Current_table



def DELCOL(Current_table) :
    print("Executing command : DELCOL")

    df = pd.read_csv(f"{Current_table}.csv")

    if not Current_table:
        print("Error: No table opened.")
        return

    df = pd.read_csv(f"{Current_table}.csv")
    print("Available columns:", ", ".join(df.columns))
    col = input("Enter column name to delete: ").strip()

    if col not in df.columns:
        print("Column not found.")
        return

    df = df.drop(columns=[col])
    df.to_csv(f"{Current_table}.csv", index=True)

    return Current_table


def DELTABLE() :
    print("Executing command : DELTABLE")
    
    name = input("Table name: ")

    if input("Type 'YES' to confirm: ").upper() == "YES" :
        print("Continuing")
    else : 
        print("use DELTABLE command again")
        return
    
    file_to_delete = f"{name}.csv"

    try:
        os.remove(file_to_delete)
        print(f"File '{file_to_delete}' deleted successfully.")
    except FileNotFoundError:
        print(f"Error: File '{file_to_delete}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    