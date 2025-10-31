
import pandas as pd
import json

def NEWTABLE() :
    print("Executing command : NEWTABLE")
    name = input("Enter new table name: ").strip()

    
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

    if not cols:
        print("No columns present , Table not created.")
        return

    df = pd.DataFrame(columns=cols)
    df.to_csv(f"{name}.csv", index=False)
    
    print(f"Table '{name}.csv' created successfully.")
    
    return