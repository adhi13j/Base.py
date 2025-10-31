
import pandas as pd
import json

def NEWTABLE() :
    print("Executing command : NEWTABLE")
    name = input("Enter new table name: ").strip()

<<<<<<< HEAD
    cols = input("Enter column names (comma separated): ").strip().split(",")
    cols = [c.strip() for c in cols if c.strip()]
=======
    
    primary_key=input("Enter primary key column name: ")
    cols = input("Enter column names (comma separated): ").split(",")
    cols = [primary_key.strip()]+[c.strip() for c in cols if c.strip()]
    
    data = {
        "primary_key": primary_key,
        "columns": cols
    }
    
    #Stores the data in a json file. So you can use primary key across files.
    with open(f"{name}.meta.json", "w") as f:
        json.dump(data, f)
>>>>>>> bcb5ea27842f47c8eec4640d08db15f6bacd157b

    if not cols:
        print("No columns present , Table not created.")
        return

    df = pd.DataFrame(columns=cols)
    df.to_csv(f"{name}.csv", index=False)
<<<<<<< HEAD
=======
    
>>>>>>> bcb5ea27842f47c8eec4640d08db15f6bacd157b
    print(f"Table '{name}.csv' created successfully.")
    
    return