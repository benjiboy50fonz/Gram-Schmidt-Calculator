# Import the needed libraries.
from calculator import calculate

from tkinter import * 

class Calculator(Frame):
    """
    The GUI class. This class does all
    the front-end stuff and uses tkinter.
    """
    
    def __init__(self):
        """
        The constructor. This is where the tkinter
        frame is built and all the widgets are a
        added.
        """
        
        master = Tk()
        master.title("Gram-Schmidt Calculator")
        
        super().__init__(master, width=400, height=600)
        
        self.configure(bg="lightgray")
        
        Label(self, text="# of Entries:", font=4, bg="lightgray").grid(row=0, column=0, sticky=W, pady=2)
        Label(self, text="# of Vectors:", font=4, bg="lightgray").grid(row=1, column=0, sticky=W, pady=2)
        
        # Add a "spacer" label.
        Label(self, text="", bg="lightgray").grid(row=4, column=0, sticky=N)
        
        self.resultLabel = Label(self, text="", bg="lightgray")
        self.resultLabel.grid(row=3, column=0, columnspan=2, sticky=N)
        
        self.rowEntryBox = Entry(self)
        self.rowEntryBox.grid(row=0, column=1)
        
        self.columnEntryBox = Entry(self)
        self.columnEntryBox.grid(row=1, column=1)
        
        Button(self, text="Generate Vectors", width=15, bg='gray', fg='white', command=lambda: self.generateVectors()).grid(row=2, column=0, sticky=W, pady=2, padx=2)
        Button(self, text="Calculate", width=15, bg='green', fg='white', command=lambda: self.calculate()).grid(row=2, column=1, sticky=W, pady=2, padx=2)
        
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
            temp = Label(self, text="X{}".format(str(i+1)), font=4, bg="lightgray")
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
        
        # Create an empty list.
        vectors = []
                
        # Clear the result label alone.
        self.resultLabel.configure(text="", bg="lightgray")
                
        # Do nothing if the size hasn't been set.
        if self.columnsNeeded == 0 or self.rowsNeeded == 0:
            return
        
        # Prepare the vectors.
        for i in range(self.columnsNeeded):
            vectors.append([])
        
        # Grab all the entries. If one doesn't exist or one has the wrong type, do nothing.
        try:
            for entry in self.entries:
                vector = entry[1]
                if "" == entry[0].get():
                    return
                vectors[vector].append(int(entry[0].get()))
                
        except(TypeError, ValueError):
            return
        
        # Calculate the resulting basis.
        result = calculate(vectors) 
        
        # Output the result to the GUI.
        self.displayResult(result)
        
    def displayResult(self, result):
        """
        Display the result in the GUI.
        This is nothing fancy.
        """
        
        # Float all the results for uniformity.
        for i in range(len(result)):
            for j in range(len(result[i])):
                result[i][j] = float(result[i][j])
        
        # Create the result string to display.
        s = ""
        c = 1
        for res in result:
            s = s + "V" + str(c) + " = {}".format(res) + "\n"
            c += 1
        
        # Display the result.
        self.resultLabel = Label(self, text=s[:-1], font=4, bg="green")
        self.resultLabel.grid(row=3, column=0, columnspan=2, sticky=N)
        
    def clear(self):
        """
        Clears all the entries in the GUI.
        """
        
        # Clear the entries.
        for entry in self.entries:
            entry[0].grid_forget()
        
        # Erase the vector labels.
        for label in self.labels:
            label.grid_forget()
        
        # Erase the result label.
        self.resultLabel.configure(text="", bg="lightgray")
        
        # Empty the entries list and the labels list.
        self.entries = []
        self.labels = []
