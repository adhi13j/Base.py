import pandas as pd

def NEWTABLE() :
    print("Executing command : NEWTABLE")
    name = input("Enter new table name: ").strip()

    cols = input("Enter column names (comma separated): ").split(",")
    cols = [c.strip() for c in cols if c.strip()]

    if not cols:
        print("No columns present , Table not created.")
        return

    df = pd.DataFrame(columns=cols)
    df.to_csv(f"{name}.csv", index=True)
    print(f"Table '{name}.csv' created successfully.")
    
    return