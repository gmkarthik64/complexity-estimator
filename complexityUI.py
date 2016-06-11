from Tkinter import *
from tkFileDialog import askopenfilename
import complexity
import importlib
import sys
import os

class Application(Frame):
    
    def __init__(self,master, filename):
        Frame.__init__(self,master)
        self.filename = filename
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        self.funText = Label(self,text ="Function Name:")
        self.funText.grid(row=0, column = 0, sticky=W)
        self.funInput = Entry(self)
        self.funInput.grid(row= 0,  column = 1, sticky=W)
        self.begText = Label(self,text ="Range Start:")
        self.begText.grid(row=1, column = 0, sticky=W)
        self.rangeBeg = Entry(self)
        self.rangeBeg.grid(row = 1, column = 1, sticky = W)
        self.endText = Label(self,text ="Range End:")
        self.endText.grid(row=2, column = 0, sticky=W)
        self.rangeEnd = Entry(self)
        self.rangeEnd.grid(row = 2, column = 1, sticky = W)
        self.stepText = Label(self,text ="Range Step:")
        self.stepText.grid(row=3, column = 0, sticky=W)
        self.rangeStep = Entry(self)
        self.rangeStep.grid(row = 3, column = 1, sticky = W)
        self.time = Button(self, text = "Time Graph", 
            command = lambda: self.genGraph(0))
        self.time.grid(row=5,column=0, sticky=W)
        self.line = Button(self, text = "Lines Executed", 
            command = lambda: self.genGraph(1))
        self.line.grid(row=5,column=1, sticky=W)
        self.func = Button(self, text = "Function Calls", 
            command = lambda: self.genGraph(2))
        self.func.grid(row=5,column=2, sticky=W)
    
    def genGraph(self, i):
        if self.filename[-3:] == ".py":
            sys.path.append(filename)
            mod = importlib.import_module(os.path.basename(self.filename)[:-3])
            try:
                f = getattr(mod, self.funInput.get())
            except:
                return
                
            if i == 0:
                complexity.timeGraph(f,int(self.rangeBeg.get()),
                    int(self.rangeEnd.get()), int(self.rangeStep.get()))
            elif i == 1:
                complexity.lineExecGraph(f,int(self.rangeBeg.get()),
                    int(self.rangeEnd.get()), int(self.rangeStep.get()))
            else:
                complexity.funCallGraph(f,int(self.rangeBeg.get()),
                    int(self.rangeEnd.get()), int(self.rangeStep.get()))
        else:
            return
    
    def on_close(self):
        self.master.destroy()
        
Tk().withdraw()
filename = askopenfilename()
root = Tk()
root.geometry("500x300")
app = Application(root,filename)

def on_close():
    root.destroy()
    sys.exit()
    
root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()

