from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import numpy as np


class WindowWeight:

    def __init__(self, input_, hidden_, output_):
        self.root = Tk()
        self.showWindow()
        self.createFrame()
        self.createControls(input_, hidden_, output_)
        self.root.mainloop()
        
    def showWindow(self):
        self.root.title("RNADelta ")
        self.root.resizable(0,0)
        self.root.iconbitmap("icono.ico")

    def createFrame(self):
        self.frame = Frame(self.root, pady=20, padx=11)
        self.frame.pack()

    def createControls(self, input_, hidden_, output_):
        self.panel = Label(self.frame)
        self.panel.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        self.panelUmbralWeight = Label(self.panel, bg="gray")
        self.panelUmbralWeight.grid(row=1, column=0, padx=5, pady=10, rowspan=2, columnspan=2)
        
        # CAPA DE ENTRADA
        if len(output_):
            self.labelTitleCE = Label(self.panelUmbralWeight, text="Pesos CE-C1", fg="white", bg="gray")
            self.labelTitleCE.grid(row=0, column=0)
            self.labelTitleCE.config(width=30, font='Helvetica 10 bold')
            self.text_areaCE = Text(self.panelUmbralWeight)
            self.text_areaCE.delete(1.0, END)  # Limpiar el área de texto
            self.text_areaCE.grid(row=1, column=0, padx=5, pady=6)
            self.text_areaCE.config(width=30, height=20)
            self.text_areaCE.insert(END, "\n")
            self.text_areaCE.insert(END, np.around(input_, decimals=4))

        # CAPAS OCULTAS
        if len(hidden_):
            self.labelTitleCO = Label(self.panelUmbralWeight, text="Pesos de las capas ocultas", fg="white", bg="gray")
            self.labelTitleCO.grid(row=0, column=1)
            self.labelTitleCO.config(width=30, font='Helvetica 10 bold')
            self.text_areaCO = Text(self.panelUmbralWeight)
            self.text_areaCO.delete(1.0, END)  # Limpiar el área de texto
            self.text_areaCO.grid(row=1, column=1, padx=5, pady=6)
            self.text_areaCO.config(width=30, height=20)

        for i in range(len(hidden_)):
            self.text_areaCO.insert(END, "\n")
            self.text_areaCO.insert(END, f"C{i+1}-C{i+2}: \n")
            self.text_areaCO.insert(END, np.around(hidden_[i], decimals=4))
            self.text_areaCO.insert(END, "\n")

        # CAPA DE SALIDA
        if len(output_):
            self.labelTitleCS = Label(self.panelUmbralWeight, text=f"Pesos C{len(hidden_)}-CS", fg="white", bg="gray")
            self.labelTitleCS.grid(row=0, column=2)
            self.labelTitleCS.config(width=30, font='Helvetica 10 bold')
            self.text_areaCS = Text(self.panelUmbralWeight)
            self.text_areaCS.delete(1.0, END)  # Limpiar el área de texto
            self.text_areaCS.grid(row=1, column=2, padx=5, pady=6)
            self.text_areaCS.config(width=30, height=20)
            self.text_areaCS.insert(END, "\n")
            self.text_areaCS.insert(END, np.around(output_, decimals=4))
        else:
            self.labelTitleCS = Label(self.panelUmbralWeight, text="Capa de salida", fg="white", bg="gray")
            self.labelTitleCS.grid(row=0, column=2)
            self.labelTitleCS.config(width=30, font='Helvetica 10 bold')
            self.text_areaCS = Text(self.panelUmbralWeight)
            self.text_areaCS.delete(1.0, END)  # Limpiar el área de texto
            self.text_areaCS.grid(row=1, column=2, padx=5, pady=6)
            self.text_areaCS.config(width=30, height=20)
            self.text_areaCS.insert(END, "\n")
            self.text_areaCS.insert(END, np.around(input_, decimals=4))
        

class WindowUmbral:

    def __init__(self, input_, hidden_, output_):
        self.root = Tk()
        self.showWindow()
        self.createFrame()
        self.createControls(input_, hidden_, output_)
        self.root.mainloop()
        
    def showWindow(self):
        self.root.title("RNADelta ")
        self.root.resizable(0,0)
        self.root.iconbitmap("icono.ico")

    def createFrame(self):
        self.frame = Frame(self.root, pady=20, padx=11)
        self.frame.pack()

    def createControls(self, input_, hidden_, output_):
        self.panel = Label(self.frame)
        self.panel.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        self.panelUmbralWeight = Label(self.panel, bg="gray")
        self.panelUmbralWeight.grid(row=1, column=0, padx=5, pady=10, rowspan=2, columnspan=2)

        # CAPAS OCULTAS
        if len(hidden_):
            self.labelTitleCO = Label(self.panelUmbralWeight, text="Umbral capas ocultas", fg="white", bg="gray")
            self.labelTitleCO.grid(row=0, column=1)
            self.labelTitleCO.config(width=30, font='Helvetica 10 bold')
            self.text_areaCO = Text(self.panelUmbralWeight)
            self.text_areaCO.delete(1.0, END)  # Limpiar el área de texto
            self.text_areaCO.grid(row=1, column=1, padx=5, pady=6)
            self.text_areaCO.config(width=30, height=20)

            self.text_areaCO.insert(END, "\n")
            self.text_areaCO.insert(END, "U1: \n")
            self.text_areaCO.insert(END, np.around(input_, decimals=4))

        for i in range(len(hidden_)):
            self.text_areaCO.insert(END, "\n")
            self.text_areaCO.insert(END, f"U{i+2}: \n")
            self.text_areaCO.insert(END, np.around(hidden_[i], decimals=4))
            self.text_areaCO.insert(END, "\n")

        # CAPA DE SALIDA
        if len(output_):
            self.labelTitleCS = Label(self.panelUmbralWeight, text="Umbral capa de salida", fg="white", bg="gray")
            self.labelTitleCS.grid(row=0, column=2)
            self.labelTitleCS.config(width=30, font='Helvetica 10 bold')
            self.text_areaCS = Text(self.panelUmbralWeight)
            self.text_areaCS.delete(1.0, END)  # Limpiar el área de texto
            self.text_areaCS.grid(row=1, column=2, padx=5, pady=6)
            self.text_areaCS.config(width=30, height=20)
            self.text_areaCS.insert(END, "\n")
            self.text_areaCS.insert(END, np.around(output_, decimals=4))
        else:
            self.labelTitleCS = Label(self.panelUmbralWeight, text="Capa de salida", fg="white", bg="gray")
            self.labelTitleCS.grid(row=0, column=2)
            self.labelTitleCS.config(width=30, font='Helvetica 10 bold')
            self.text_areaCS = Text(self.panelUmbralWeight)
            self.text_areaCS.delete(1.0, END)  # Limpiar el área de texto
            self.text_areaCS.grid(row=1, column=2, padx=5, pady=6)
            self.text_areaCS.config(width=30, height=20)
            self.text_areaCS.insert(END, "\n")
            self.text_areaCS.insert(END, np.around(input_, decimals=4))
        

