import pandas as pd
import os


def DISPLAYTABLE(Current_table) :

    print("Executing command : OPENTABLE")
    
    if not os.path.exists(f"{Current_table}.csv"):
       print("Error: Table not found.")
       return
    
    #for now it is shows only head for testing

    df = pd.read_csv(f"{Current_table}.csv")

    df.head()
    
    