import pandas as pd


def ADD (Current_table) :
    print("Executing command : ADD")
    
    if not Current_table:
        print("Error: No table opened.")
        return

    is_primary = input("is the column primary key : ")
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
