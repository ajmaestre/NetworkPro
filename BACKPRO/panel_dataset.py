from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk

def createPanelDataset(frame, charge_CSV):
    panelDataset = Label(frame, bg="gray")
    panelDataset.grid(row=1, column=0, padx=5, pady=10, rowspan=2, columnspan=2)
    panelDataset.config(width=250, height=200)
    # Area de texto de las entradas
    labelTitleE = Label(panelDataset, text="Entradas", fg="white", bg="gray")
    labelTitleE.grid(row=0, column=0)
    labelTitleE.config(width=20, font='Helvetica 10 bold')
    text_areaE = Text(panelDataset)
    text_areaE.delete(1.0, END)  # Limpiar el área de texto
    text_areaE.grid(row=1, column=0, padx=5, pady=6)
    text_areaE.config(width=20, height=16)
    # Area de texto de las salidas
    labelTitleS = Label(panelDataset, text="Salidas", fg="white", bg="gray")
    labelTitleS.grid(row=0, column=1)
    labelTitleS.config(width=20, font='Helvetica 10 bold')
    text_areaS = Text(panelDataset)
    text_areaS.delete(1.0, END)  # Limpiar el área de texto
    text_areaS.grid(row=1, column=1, padx=5, pady=6)
    text_areaS.config(width=20, height=16)
    # BOTOB CARGAR DATASET
    panelBtnInsert = Label(panelDataset, bg="gray")
    panelBtnInsert.grid(row=2, column=0, padx=5, pady=0, columnspan=2)
    panelBtnInsert.config(width=20, height=5)
    btnInsert = Button(panelBtnInsert, text="Cargar entradas y salidas", command=charge_CSV)
    btnInsert.grid(row=0, column=0)
    btnInsert.config(padx=20, pady=4, width=36)
    btnInsert.config(bg="green3", foreground="white", font='Helvetica 10 bold')

    return panelDataset, text_areaS, text_areaE