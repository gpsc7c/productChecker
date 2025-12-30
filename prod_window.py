#This is the function/class file for the tkinter window and related functions
import tkinter as tk
#tkinter setup (should be moved to a new import)
root = tk.Tk()
root.title("Cost and Stock Checker")
ENTRYTEXT = tk.StringVar(value = "Enter URLs/Products here.")
ENTRY = tk.Entry(root, textvariable = ENTRYTEXT)
entryString = ENTRY.get()
ENTRY.pack()
ADD = tk.Button(root, text = "Add")
ADD.pack()
REMOVE = tk.Button(root, text = "Remove")
REMOVE.pack()
