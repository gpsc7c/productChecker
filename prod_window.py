#This is the function/class file for the tkinter window and related functions
import tkinter as tk
#tkinter window setup 
root = tk.Tk()
root.title("Cost and Stock Checker")

#Entry field (with dropdown) allows user to add new entries, search to see if an entry exists, 
#force check on existing entries, and remove existing entries
FRAMELEFTTOP = tk.Frame(root)
FRAMELEFTTOP.pack(side=tk.TOP, anchor = "w")
FRAMELEFTBOTTOM = tk.Frame(root)
FRAMELEFTBOTTOM.pack(side=tk.LEFT)
FRAMERIGHT = tk.Frame(root)
FRAMERIGHT.pack(side=tk.RIGHT, expand=True)

#left top pane with buttons
ENTRYTEXT = tk.StringVar(value = "Enter URLs/Products here.")
ENTRY = tk.Entry(FRAMELEFTTOP, textvariable = ENTRYTEXT)
entryString = ENTRY.get()
ENTRY.pack(side = tk.TOP, anchor = "nw")
ADD = tk.Button(FRAMELEFTTOP, text = "Add")
ADD.pack(side = tk.LEFT)
SEARCH = tk.Button(FRAMELEFTTOP, text = "Search")
SEARCH.pack(side = tk.LEFT)
CHECK = tk.Button(FRAMELEFTTOP, text = "Check")
CHECK.pack(side = tk.LEFT)
REMOVE = tk.Button(FRAMELEFTTOP, text = "Remove")
REMOVE.pack(side = tk.LEFT)

#left bottom pane with text of open file
VSCROLL = tk.Scrollbar(FRAMELEFTBOTTOM, orient = tk.VERTICAL)
VSCROLL.pack(side=tk.RIGHT, fill=tk.Y)
HSCROLL = tk.Scrollbar(FRAMELEFTBOTTOM, orient = tk.HORIZONTAL)
HSCROLL.pack(side=tk.BOTTOM, fill=tk.X)
TEXTBOX = tk.Text(FRAMELEFTBOTTOM,
                  wrap=tk.NONE, #here to prevent line wrapping
                  yscrollcommand=VSCROLL.set,
                  xscrollcommand=HSCROLL.set)
TEXTBOX.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
VSCROLL.config(command=TEXTBOX.yview)
HSCROLL.config(command=TEXTBOX.xview)

#limits size of window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("{}x{}+{}+{}".format(round(screen_width/2), round(screen_height/2), round(screen_width/4), round(screen_height/4)))
