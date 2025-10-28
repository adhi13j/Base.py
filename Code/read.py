import pandas as pd
import os


def OPENTABLE(Current_table) :

    print("Executing command : OPENTABLE")
    name = input("Table name: ").strip()
    
    if not os.path.exists(f"{name}.csv"):
       print("Error: Table not found.")
       return
    

    Current_table = name
    return Current_table