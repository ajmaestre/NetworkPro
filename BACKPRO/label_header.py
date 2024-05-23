from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk


def createLabelEntrada(frame):
    labelEntradas = Label(frame, text="N° Entradas", fg="blue")
    labelEntradas.grid(row=0, column=0, padx=5, pady=5)
    labelEntradas.config(width=10, font='Helvetica 12 bold')
    txtEntradas = Entry(frame, fg="red", justify=CENTER)
    txtEntradas.grid(row=0, column=1, padx=5, pady=5)
    txtEntradas.config(width=10, font='Helvetica 12 bold')
    return txtEntradas

def createLabelSalida(frame):
    labelSalidas = Label(frame, text="N° Salidas", fg="blue")
    labelSalidas.grid(row=0, column=2, padx=5, pady=5)
    labelSalidas.config(width=10, font='Helvetica 12 bold')
    txtSalidas = Entry(frame, fg="red", justify=CENTER)
    txtSalidas.grid(row=0, column=3, padx=5, pady=5)
    txtSalidas.config(width=10, font='Helvetica 12 bold')
    return txtSalidas

def createLabelPatrones(frame):
    labelPatrones = Label(frame, text="N° Patrones", fg="blue")
    labelPatrones.grid(row=0, column=4, padx=5, pady=5)
    labelPatrones.config(width=10, font='Helvetica 12 bold')
    txtPatrones = Entry(frame, fg="red", justify=CENTER)
    txtPatrones.grid(row=0, column=5, padx=5, pady=5)
    txtPatrones.config(width=10, font='Helvetica 12 bold')
    return txtPatrones