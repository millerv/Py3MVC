from tkinter import *
from tkinter import ttk

class MyFrame(ttk.Frame):
    '''
    The MyFrame class holds all the GUI information.

    Args:
        arg (controller): The arg is a TestController object that acts as the Controller in MVC model.

    Attributes:
        arg (controller): Where we store the controller passed in.
    '''
    def __init__(self, controller):
        ttk.Frame.__init__(self, padding = "3 3 12 12")
        self.grid(column=0, row=0, sticky=(N,W,E,S))
        self.pack()
        self.controller = controller
        self.controller.root.title("Feet to Meters")
        self.controller.root.columnconfigure(0, weight=1)
        self.controller.root.rowconfigure(0, weight=1)

        # Menubar setup
        self.menubar = Menu(self.controller.root)

        # Create dropdown menus
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open...") # no command yet
        self.filemenu.add_command(label="Save") # no command yet
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # Create edit menu
        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Cut") # no command yet
        self.editmenu.add_command(label="Copy") # no command yet
        self.editmenu.add_command(label="Paste") # no command yet
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        # Create help menu
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About") # no command yet
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        # show menubar
        self.controller.root.config(menu=self.menubar)

        #Output Label
        self.temp = StringVar()
        self.temp.set("???")
        self.outputLabel = ttk.Label(self, textvariable=self.temp).grid(column=2, row=2, sticky=(W,E))

        #Entry Space
        self.feetEntry = ttk.Entry(self, width=7)
        self.feetEntry.insert(0,"0")
        self.feetEntry.grid(column=2, row=1, sticky=(W,E))
        self.feetEntry.bind('<Return>', self.controller.buttonPressed1)

        self.convertButton2 = ttk.Button(self, text="Calculate", command=self.controller.buttonPressed1).grid(column=2, row=3, sticky=W)

        # New text
        ttk.Label(self, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(self, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(self, text="meters").grid(column=3, row=2, sticky=W)

        #Quit button
        ttk.Button(self, text="Quit", command=self.quit).grid(column=3, row=3, sticky=W)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.feetEntry.focus()
