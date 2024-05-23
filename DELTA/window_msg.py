from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk


def showWindow():
    root.title("RNADelta ")
    root.resizable(0,0)
    root.iconbitmap("icono.ico")


def createFrame():
    global frame
    frame = Frame(root, width=450, height=350, pady=20, padx=11)
    frame.pack()
    return frame


def createControls(title, message):
    global panelImage
    global panel
    global panelMessage

    panel = Label(frame)
    panel.grid(row=1, column=0, padx=5, pady=5, columnspan=2)
    panel.config(width=300, height=200)

    panelMessage = Label(panel, bg="gray")
    panelMessage.grid(row=1, column=2, padx=5, pady=5, columnspan=2)
    panelMessage.config(width=300, height=200)

    labelTitle = Label(panelMessage, text=title, fg="white", bg="gray")
    labelTitle.grid(row=0, column=0, padx=5, pady=5)
    labelTitle.config(width=10, font='Helvetica 14 bold')

    labelMessage = Label(panelMessage, text=message, fg="white", bg="gray")
    labelMessage.grid(row=1, column=0, padx=5, pady=5)
    labelMessage.config(width=50, font='Helvetica 12 bold')


def createWind(title, message):
    global root
    root = Tk()
    showWindow()
    createFrame()
    createControls(title, message)
    root.mainloop()
