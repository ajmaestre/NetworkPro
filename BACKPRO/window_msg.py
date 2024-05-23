from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk


class WindowMsg:

    def __init__(self, title, message):
        self.root = Tk()
        self.showWindow()
        self.createFrame()
        self.createControls(title, message)
        self.root.mainloop()
        
    def showWindow(self):
        self.root.title("RNADelta ")
        self.root.resizable(0,0)
        self.root.iconbitmap("icono.ico")


    def createFrame(self):
        self.frame = Frame(self.root, width=450, height=350, pady=20, padx=11)
        self.frame.pack()


    def createControls(self, title, message):

        self.panel = Label(self.frame)
        self.panel.grid(row=1, column=0, padx=5, pady=5, columnspan=2)
        self.panel.config(width=300, height=200)

        self.panelMessage = Label(self.panel, bg="gray")
        self.panelMessage.grid(row=1, column=2, padx=5, pady=5, columnspan=2)
        self.panelMessage.config(width=300, height=200)

        self.labelTitle = Label(self.panelMessage, text=title, fg="white", bg="gray")
        self.labelTitle.grid(row=0, column=0, padx=5, pady=5)
        self.labelTitle.config(width=10, font='Helvetica 14 bold')

        self.labelMessage = Label(self.panelMessage, text=message, fg="white", bg="gray")
        self.labelMessage.grid(row=1, column=0, padx=5, pady=5)
        self.labelMessage.config(width=50, font='Helvetica 12 bold')

        
