from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk


def createPanelPredict(frame):
    panelPredict = Label(frame, bg="gray")
    panelPredict.grid(row=5, column=4, padx=1, pady=1, columnspan=2, rowspan=4)
    return panelPredict

def createGroupInputPredict(frame, panelPredict, predict):
    panelTxtPredict = Label(panelPredict, bg="gray")
    panelTxtPredict.grid(row=0, column=0, padx=1, pady=1, columnspan=2)
    txtPredict = Entry(panelTxtPredict, fg="black", justify=CENTER)
    txtPredict.grid(row=0, column=0, padx=2, pady=2)
    txtPredict.config(width=15, font='Helvetica 16 bold')
    panelBtnPredict = Label(panelPredict, bg="gray")
    panelBtnPredict.grid(row=0, column=2, padx=1, pady=1)
    btnPredict = Button(panelBtnPredict, text="Predecir", command=predict)
    btnPredict.grid(row=0, column=0)
    btnPredict.config(padx=1, pady=2, width=12)
    btnPredict.config(bg="green3", foreground="white", font='Helvetica 10 bold')
    return txtPredict

def createGroupInputResult(frame, panelPredict):
    panelLabelResult= Label(panelPredict, bg="gray")
    panelLabelResult.grid(row=1, column=0, padx=1, pady=1)
    labelResult = Label(panelLabelResult, text="Predicción", fg="white", bg="gray")
    labelResult.grid(row=0, column=0, padx=2, pady=2)
    labelResult.config(width=12, font='Helvetica 10 bold')
    panelTxtResult= Label(panelPredict, bg="gray")
    panelTxtResult.grid(row=1, column=1, padx=1, pady=1, columnspan=2)
    txtResult = Entry(panelTxtResult, fg="black", justify=CENTER)
    txtResult.grid(row=0, column=0, padx=2, pady=5)
    txtResult.config(width=15, font='Helvetica 16 bold') 
    return txtResult      
