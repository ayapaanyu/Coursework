### Aya Ishida (MSc IT) 
### ISD Term2 Coursework 3, Submitted at 1/4/2016

from tkinter import Tk, Label, Button, Frame, LEFT, Canvas, StringVar
from tkinter.filedialog  import askopenfilename
from tkinter.messagebox import showerror, showinfo

class Display(Frame):
    ##Constructor
    def __init__(self, master = None):
        Frame.__init__(self, master)
        ## Canvas to display junctions
        self.c = Canvas(master, width=600, height=600, bd=0.5, relief="groove")
        self.c.pack(side=LEFT)
        ## Event when clicking on the canvas
        self.c.bind ("<Button-1>", self.updateLabel)
        ## Button to open a file
        Button (self, text = "open", command = self.getFile).pack()
        ## Label to display a junction name
        self.v = StringVar()
        Label (self, textvariable = self.v, width = 10, height= 1, bd = 0.5, relief="groove").pack()

        self.pack()
        
    ## (1) Open a file with the button
    def getFile(self):
        filename = askopenfilename (parent = self, title = "Please select a file")

        ## if a file is selected, read the contents, 
        if (len(filename) > 0):
            inf = open(filename, "r")
            lines = inf.readlines()

            i = 0
            self.curLine = []
            for lines[i] in lines:
                item = lines[i].rstrip("\n")
                self.curLine.append(item)
                i = i + 1

            ## and check if it has got "Connector Network" or "Pipe Network" on the first line.
            ## if Yes, Go to (2)Draw junctions on the canvas
            ## if No, it displays an error. 
            if (self.curLine[0] == "Connector Network"):
                self.erase()
                self.draw()
            elif (self.curLine[0] == "Pipe Network"):
                self.erase()
                self.draw()           
            else:
                self.erase()
                showerror("Error", "File could not be read")
                
        ## if a file is not selected, it displays an error
        else:
            self.erase()
            showinfo("showinfo", "Choose a file")

    ## (2) Draw junctions on the canvas
    def erase(self): ## delete all on the canvas
        self.c.delete("all")
        self.v.set ("")

    def draw(self): ## draw on the canvas and the label
        i = 2
        self.junList = []
        
        ## Take the line between Junctions Start and Junctions End,
        ## and draw a circle and label of the junction.
        while i < self.curLine.index ("Junctions END"):
            junLine = self.curLine[i].split(",")
            junName = junLine[0]
            x = junLine[1]
            y = junLine[2]
            self.c.create_oval(int(x)-5, int(y)-5, int(x)+5, int(y)+5, width=0, fill="yellow")
            self.c.create_text(int(x), int(y)-15, text = str(junName))
            
            ## Keep this Junction data as a junList for the next process (3). 
            self.junList.append (junLine[0])
            self.junList.append (junLine[1])
            self.junList.append (junLine[2])

            i = i + 1

    ## (3) Display a junction name on the label when clicked.
    def updateLabel(self, event):
        i = 0
        
        ## Take a junction name, point x and y of junction data in junList,
        ## if the clicked point is within 5 distance of the point x and y,
        ## update the label with the junction name.
        while i < len(self.junList):
            junName = self.junList[i]
            pointX = self.junList[i+1]
            pointY = self.junList[i+2]
            if abs(event.x - int(pointX)) <= 5 and abs(event.y - int(pointY)) <= 5:
                    self.v.set (junName)
                    break
                
            ## if not, the label displays nothing.
            else:
                self.v.set ("")
                i = i + 3

if __name__ == "__main__":
    Display().mainloop()
