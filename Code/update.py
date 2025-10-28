import pandas as pd


def ADD (Current_table) :
    print("Executing command : ADD")
    
    if not Current_table:
        print("Error: No table opened.")
        return

    
    columns = list(pd.read_csv(f'{Current_table}.csv').columns)
    
    row_data = {}  

    for column in columns :
        data_input = input(f"value for column {column}: ")
        row_data[f"{column}"] = data_input
        
    row_df = pd.DataFrame([row_data])
    row_df.to_csv(f'{Current_table}.csv', mode='a', index=False, header=False)

    return Current_table


def ADDCOL(Current_table) :
    print("Executing command : ADDCOL ")

    df = pd.read_csv(f"{Current_table}.csv")

    col_name = input("Enter new column name: ").strip()
    default_val = input("Default value: ")

    df[col_name] = default_val
    df.to_csv(f"{Current_table}.csv", index=False)

    return Current_table