# This is Main, and the primary executable's core
from datetime import datetime
import os
import tkinter as tk
#tkinter setup
root = tk.Tk()
root.title = "costChecker"
entry = tk.Entry(root)
entryString = entry.get()

def fileCreation(file_name = "ProductsFile.txt"):
    dir_name = os.path.dirname(os.path.realpath(__file__))
    full_path = os.path.join(dir_name, file_name)
    return full_path

def Main():
    #tracks when the program started running
    start_time = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    print(f"---------------------------\nRun at {start_time}\n---------------------------\n")
    ######
    #NEED TO CHECK IF WE OPENED VIA STARTUP OR USER
    #USER FIRST
    ######

    #creates or opens the file----------
    prods_file = open(fileCreation(), 'a')
    #-----------------------------------
    while(True):
        break
    #_______________________________________________________________________
    #
    #CHECK FOR A FILE
    #_______________________________________________________________________
    #_______________________________________________________________________
    #
    #MAKE A FILE IF NOT PRESENT, THEN/OTHERWISE OPEN THE FILE FOR EDITING
    #_______________________________________________________________________
    #_______________________________________________________________________
    #
    #CHECK IF THE FILE HAS CHANGED
    #_______________________________________________________________________
    #_______________________________________________________________________
    #
    #HAVE FLAG FOR IF THE USER HAS ADDED TO THE FILE SINCE LAST LOOP, 
    #IT HAS BEEN 30 MINUTES SINCE LAST CHECK,
    #OR IT IS THE FIRST LOOP, DO THE FOLLOWING
    #_______________________________________________________________________
    #_______________________________________________________________________
    #
    ##UPDATE THE FILE WITH ANYTHING THE USER REQUESTED
    #_______________________________________________________________________
    #_______________________________________________________________________
    #
    ##LOOP TO CHECK THE FILE FOR EACH URL
    #_______________________________________________________________________
    #_______________________________________________________________________
    ##LOOP TO CHECK THE FILE FOR EACH PRODUCT, PROMPT THE USER WITH URLS
    ##TO CHECK IF IT IS FINDING THE RIGHT ITEMS, THEN CONVERT TO URLS
    #_______________________________________________________________________





    
    #tracks when the program ended running
    end_time = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    print(f"\n--------------------------------\nFinished at {end_time}\n--------------------------------")
    pass

if __name__ == "__main__":
    Main()
