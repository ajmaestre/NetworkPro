from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk


def createPanelWeightAndUmbral(frame, getWeightEnd, getUmbralEnd, getWeightInit, getUmbralInit):
    panelBorder = Label(frame, bg="gray")
    panelBorder.grid(row=5, column=0, padx=1, pady=1, columnspan=2, rowspan=4)
    # BOTON PARA LOS UMBRALES INICIALES
    panelBtnUmbralInit = Label(panelBorder, bg="gray")
    panelBtnUmbralInit.grid(row=0, column=0, padx=1, pady=2)
    btnUmbralInit = Button(panelBtnUmbralInit, text="Umbrales iniciales", command=getUmbralInit)
    btnUmbralInit.grid(row=0, column=0)
    btnUmbralInit.config(padx=1, pady=4, width=20)
    btnUmbralInit.config(bg="green3", foreground="white", font='Helvetica 10 bold')
    # BOTON PARA LOS PESOS INICIALES
    panelBtnWeightInit = Label(panelBorder, bg="gray")
    panelBtnWeightInit.grid(row=0, column=1, padx=1, pady=2)
    btnWeightInit = Button(panelBtnWeightInit, text="Pesos iniciales", command=getWeightInit)
    btnWeightInit.grid(row=0, column=0)
    btnWeightInit.config(padx=1, pady=4, width=20)
    btnWeightInit.config(bg="green3", foreground="white", font='Helvetica 10 bold')
    # BOTON PARA LOS UMBRALES FINALES
    panelBtnUmbralEnd = Label(panelBorder, bg="gray")
    panelBtnUmbralEnd.grid(row=1, column=0, padx=1, pady=2)
    btnUmbralEnd = Button(panelBtnUmbralEnd, text="Umbrales finales", command=getUmbralEnd)
    btnUmbralEnd.grid(row=0, column=0)
    btnUmbralEnd.config(padx=1, pady=4, width=20)
    btnUmbralEnd.config(bg="green3", foreground="white", font='Helvetica 10 bold')
    # BOTON PARA LOS PESOS FINALES
    panelBtnWeightEnd = Label(panelBorder, bg="gray")
    panelBtnWeightEnd.grid(row=1, column=1, padx=1, pady=2)
    btnWeightEnd = Button(panelBtnWeightEnd, text="Pesos finales", command=getWeightEnd)
    btnWeightEnd.grid(row=0, column=0)
    btnWeightEnd.config(padx=1, pady=4, width=20)
    btnWeightEnd.config(bg="green3", foreground="white", font='Helvetica 10 bold')
