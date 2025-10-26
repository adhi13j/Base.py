import pandas as pd
import time
import csv
import os

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
    return

def ADDCOl() :
    print("Executing command : ADDCOL")
    dataType = input("dataType of new column :").lower()
    
    return
def DELCOl() :
    print("Executing command : DELCOL ")
    return

def NEWTABLE() :
    print("Executing command : NEWTABLE")
    return
def OPENTABLE() :
    print("Executing command : OPENTABLE")
    name = input("Table name")
    global Current_table
    Current_table = pd.read_csv(f"{name}.csv")
    return
def DELTABLE() :
    print("Executing command : DELTABLE")
    
    name = input("Table name")

    if input("Type 'YES' to confirm").upper() == "YES" :
        print("Continuing")
    else : 
        print("use DELTABLE command again")
        return
    
    file_to_delete = f"{name}.txt"

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