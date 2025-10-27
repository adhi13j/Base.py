import pandas as pd
import time
import csv
import os

Current_table=None
Running=True

Commands = [
    "ADD" , 
    "DEL" ,
    "ADDCOl" ,
    "DELCOl" ,

    "NEWTABLE" ,
    "OPENTABLE" ,
    "DELTABLE" ,
]
# usefull to get String input and numeric input


def check_input_type(user_input):
    try:
        # Attempt to convert to an integer
        int(user_input)
        return "Number (integer)"
    except ValueError:
        try:
            # Attempt to convert to a float if not an integer
            float(user_input)
            return "Number (float)"
        except ValueError:
            return "String"

def ADD () :
    print("Executing command : ADD")
    
    global Current_table
    
    if not Current_table:
        print("Error: No table opened.")
        return

    
    columns = list(pd.read_csv(f'{Current_table}.csv').columns)
    
    row_data = {}  

    for column in columns :
        data_input = input(f"value for column {column}")
        row_data[f"{column}"] = data_input
        
    row_df = pd.DataFrame([row_data])
    row_df.to_csv(f'{Current_table}.csv', mode='a', index=False, header=False)

    return
def DEL () :
    print("Executing command : DEL")
    
    global Current_table
    
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
    df.to_csv(f"{Current_table}.csv", index=False)

    return
def ADDCOl() :
    print("Executing command : ADDCOL ")

    global Current_table
    df = pd.read_csv(f"{Current_table}.csv")

    col_name = input("Enter new column name: ").strip()
    default_val = input("Default value: ")

    df[col_name] = default_val
    df.to_csv(f"{Current_table}.csv", index=False)

    return

def DELCOl() :
    print("Executing command : DELCOL")

    global Current_table
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
    df.to_csv(f"{Current_table}.csv", index=False)

    return

def NEWTABLE() :
    print("Executing command : NEWTABLE")
    name = input("Enter new table name: ").strip()

    cols = input("Enter column names (comma separated): ").split(",")
    cols = [c.strip() for c in cols if c.strip()]

    if not cols:
        print("No columns present , Table not created.")
        return

    df = pd.DataFrame(columns=cols)
    df.to_csv(f"{name}.csv", index=False)
    print(f"Table '{name}.csv' created successfully.")

def OPENTABLE() :

    print("Executing command : OPENTABLE")
    name = input("Table name: ").strip()
    
    if not os.path.exists(f"{name}.csv"):
       print("Error: Table not found.")
       return
    
    global Current_table
    Current_table = name
    return

def DELTABLE() :
    print("Executing command : DELTABLE")
    
    name = input("Table name")

    if input("Type 'YES' to confirm").upper() == "YES" :
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

    return

def STOP() :
    global Running
    Running = False
    return

#clear cmd
os.system("cls")

Running = True

Current_table = None

def MainLoop() :

    while Running :

        os.system("cls")

        print(
        """
        ____           _____ ______   _____       
        |  _ \   /\    / ____|  ____| |  __ \      
        | |_) | /  \  | (___ | |__    | |__) |   _ 
        |  _ < / /\ \  \___ \|  __|   |  ___/ | | |
        | |_) / ____ \ ____) | |____ _| |   | |_| |
        |____/_/    \_\_____/|______(_)_|    \__, |
                                            __/ |
                                            |___/ 
        """)

        print(f"Current table : {Current_table}" if Current_table else "please use OPENTABLE to set Current table")

        print("Input Your Command : ") 

        print(
        """
        Commands :
            "ADD" 
            "DEL"
            "ADDCOl"
            "DELCOl"

            "NEWTABLE"
            "OPENTABLE"
            "DELTABLE"
            "Stop"
        """)

        command = input("Command : ").strip().upper()

        if command == "STOP":
            STOP()
        elif command in Commands:
            # calls the function with the same name
            globals()[command]()  
        else:
            print("Unknown command.")
            time.sleep(1)


if __name__ == "__main__" :
    MainLoop()