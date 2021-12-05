# Import the needed libraries.
from tkinter.font import BOLD
from calculator import calculate

from tkinter import * 

class Calculator(Frame):
    """
    The GUI class. This class does all
    the front-end stuff and uses tkinter.
    """
    
    def __init__(self, master=None):
        """
        The constructor. This is where the tkinter
        frame is built and all the widgets are a
        added.
        """
        
        super().__init__(master, width=400, height=600)
        
        Label(self, text="# of Entries:", font=4).grid(row=0, column=0, sticky=W, pady=2)
        Label(self, text="# of Vectors:", font=4).grid(row=1, column=0, sticky=W, pady=2)
        
        self.rowEntryBox = Entry(self)
        self.rowEntryBox.grid(row=0, column=1)
        
        self.columnEntryBox = Entry(self)
        self.columnEntryBox.grid(row=1, column=1)
        
        Button(self, text="Generate Vectors", width=15, bg='gray', fg='white', command=lambda: self.generateVectors()).grid(row=2, column=0, sticky=W, pady=2)
        Button(self, text="Calculate", width=15, bg='green', fg='white', command=lambda: self.calculate()).grid(row=2, column=1, sticky=W, pady=2)
        
        # Set the default dimensions.
        self.rowsNeeded = 0
        self.columnsNeeded = 0
        
        # The entry boxes for the vectors.
        self.entries = []
        self.labels = []
        self.rowPositions = []
        self.columnPoisitions = []
        
        self.grid()
        
    def generateVectors(self):
        """
        Reads the dimensions from their respective
        entry boxes. Then, it uses it to generate 
        empty vectors.
        """
        
        # First, remove the current entries.
        self.clear()
        
        # Where should we start displaying the entries?
        startRow = 0
        startColumn = 2
        
        # Grab the dimensions to make. 
        self.rowsNeeded = self.rowEntryBox.get()
        self.columnsNeeded = self.columnEntryBox.get()
        
        # Did the user enter an integer? If not, don't do anything.
        try:
            self.rowsNeeded = int(self.rowsNeeded)
            self.columnsNeeded = int(self.columnsNeeded)
        except ValueError:
            return         
        
        # Add titles.
        for i in range(self.columnsNeeded):
            temp = Label(self, text="V{}".format(str(i+1)))
            temp.grid(row=startRow, column=startColumn+i, sticky=N, padx=4)
            self.labels.append(temp)
        
        # Increment it since we just added vector names.
        startRow += 1
        
        # Clear the self.entries list and the position lists.
        self.entries = []
        
        # Add the entries.
        for i in range(self.rowsNeeded):
            for j in range(self.columnsNeeded):
                e = Entry(self, width=10)
                e.grid(row=startRow + i, column=startColumn + j, padx=4)
                self.entries.append([e, j])
                
    def calculate(self):
        """
        Grab the input entries and put them in
        a list that the calculator script can 
        use.
        """
            
        vectors = []
                
        if self.columnsNeeded == 0 or self.rowsNeeded == 0:
            return
        
        for i in range(self.columnsNeeded):
            vectors.append([])
        
        try:
            for entry in self.entries:
                vector = entry[1]
                if '' == entry[0].get():
                    return
                vectors[vector].append(int(entry[0].get()))
                
        except(TypeError):
            return
            
        result = calculate(vectors) 
        
        # Output the result to the GUI.
        self.displayResult(result)
        
    def displayResult(self, result):
        """
        Display the result in the GUI.
        This is nothing fancy.
        """
        
        for i in range(len(result)):
            for j in range(len(result[i])):
                result[i][j] = float(result[i][j])
        
        Label(self, text="Result:\n{}".format(result)).grid(row=3, column=0, columnspan=2, sticky=N)
        
    def clear(self):
        """
        Clears all the entries in the GUI.
        """
        
        for entry in self.entries:
            entry[0].grid_forget()
        
        for label in self.labels:
            label.grid_forget()
        
        self.entries = []
        self.labels = []
                                
Calculator().mainloop()