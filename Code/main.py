import pandas as pd
import time
import csv
import os

#Python files containing CRUD operations. Check Commands dict for classification details.
import create
import read
import update
import delete

Current_table=None
Running=True


#Here structure is [command : File.command, if it needs Current table as parameter] - will be used in main to pass Current table to relevant functions.
Commands = {
    "ADD" : (update.ADD,True) , 
    "DEL" : (delete.DEL,True),
    "ADDCOL" : (update.ADDCOL,True) ,
    "DELCOL" : (delete.DELCOL,True) ,

    "NEWTABLE": (create.NEWTABLE,False) ,
    "OPENTABLE": (read.OPENTABLE,True) ,
    "DELTABLE": (delete.DELTABLE,True) ,
}


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

        global Current_table
        
        if Current_table:
            print(f"Current table : {Current_table}")
        else:
            print("Please use OPENTABLE to set Current table")

        print("Input Your Command : ") 

        print(
        """
        Commands :
            "ADD" 
            "DEL"
            "ADDCOL"
            "DELCOL"

            "NEWTABLE"
            "OPENTABLE"
            "DELTABLE"
            "Stop"
        """)

        command = input("Command : ").strip().upper()

        if command == "STOP":
            STOP()
        elif command in Commands:
    
            # check if it needs Current_table
            if Commands[command][1]==True:
                result=Commands[command][0](Current_table)

            else:
                result=Commands[command][0]()
                
            #Update current_table to whatever value the function returned.
            if result is not None:
                Current_table=result

    
        else:
            print("Unknown command.")
            time.sleep(1)


if __name__ == "__main__" :
    MainLoop()