#This is the function/class file for the tkinter window and related functions
import tkinter as tk
#tkinter window setup 
root = tk.Tk()
root.title("Cost and Stock Checker")

#Entry field (with dropdown) allows user to add new entries, search to see if an entry exists, 
#force check on existing entries, and remove existing entries
ENTRYTEXT = tk.StringVar(value = "Enter URLs/Products here.")
ENTRY = tk.Entry(root, textvariable = ENTRYTEXT)
entryString = ENTRY.get()
ENTRY.pack()
ADD = tk.Button(root, text = "Add")
ADD.pack()
SEARCH = tk.Button(root, text = "Search")
SEARCH.pack()
CHECK = tk.Button(root, text = "Check")
CHECK.pack()
REMOVE = tk.Button(root, text = "Remove")
REMOVE.pack()

#limits size of window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("{}x{}+{}+{}".format(round(screen_width/2), round(screen_height/2), round(screen_width/4), round(screen_height/4)))
