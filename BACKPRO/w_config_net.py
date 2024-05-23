from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from window_msg import *


class WindowConfigNet:

    def __init__(self, epochs, learning_rate, tol, entradas, salidas, patrones, list_hidden_layers, list_hidden_functions):
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.tol = tol
        self.entradas = entradas
        self.salidas = salidas
        self.patrones = patrones
        self.list_hidden_layers = list_hidden_layers
        self.list_hidden_functions = list_hidden_functions
        self.root = Tk()
        self.showWindow()
        self.createFrame()
        self.createControls()
        self.root.mainloop()

    def showWindow(self):
        self.root.title("RNADelta ")
        self.root.resizable(0,0)
        self.root.iconbitmap("icono.ico")

    def createFrame(self):
        self.frame = Frame(self.root, pady=20, padx=11)
        self.frame.pack()

    def createControls(self):
        self.list_combo = []
        self.list_text = []

        self.panel = Label(self.frame)
        self.panel.grid(row=1, column=2, padx=5, pady=2)

        self.panelBorderHead = Label(self.panel, bg="gray")
        self.panelBorderHead.grid(row=0, column=0, padx=0, pady=10, columnspan=2, rowspan=2)
        self.panelBorderHead.config(width=300, height=20)

        self.labelEntradas = Label(self.panelBorderHead, text=f"Entradas: {self.entradas}", fg="white", bg="gray")
        self.labelEntradas.grid(row=0, column=0, padx=5, pady=5)
        self.labelEntradas.config(width=20, font='Helvetica 10 bold')

        self.labelSalidas = Label(self.panelBorderHead, text=f"Salidas: {self.salidas}", fg="white", bg="gray")
        self.labelSalidas.grid(row=0, column=1, padx=5, pady=5)
        self.labelSalidas.config(width=20, font='Helvetica 10 bold')

        self.labelPatrones = Label(self.panelBorderHead, text=f"Patrones: {self.patrones}", fg="white", bg="gray")
        self.labelPatrones.grid(row=0, column=2, padx=5, pady=5)
        self.labelPatrones.config(width=20, font='Helvetica 10 bold')

        self.panelBorderMidle = Label(self.panel, bg="gray")
        self.panelBorderMidle.grid(row=2, column=0, padx=0, pady=10, columnspan=2, rowspan=2)
        self.panelBorderMidle.config(width=300, height=20)

        self.labelIters = Label(self.panelBorderMidle, text=f"Iteraciones: {self.epochs}", fg="white", bg="gray")
        self.labelIters.grid(row=0, column=0, padx=5, pady=5)
        self.labelIters.config(width=20, font='Helvetica 10 bold')

        self.labelLearningRate = Label(self.panelBorderMidle, text=f"Tasa de aprendizaje: {self.learning_rate}", fg="white", bg="gray")
        self.labelLearningRate.grid(row=0, column=1, padx=5, pady=5)
        self.labelLearningRate.config(width=20, font='Helvetica 10 bold')

        self.labelTol = Label(self.panelBorderMidle, text=f"Tolerancia: {self.tol}", fg="white", bg="gray")
        self.labelTol.grid(row=0, column=2, padx=5, pady=5)
        self.labelTol.config(width=20, font='Helvetica 10 bold')

        self.panelBorder = Label(self.panel, bg="gray")
        self.panelBorder.grid(row=4, column=0, padx=0, pady=10, columnspan=2, rowspan=2)
        self.panelBorder.config(width=300, height=20)

        self.labelTitle = Label(self.panelBorder, text="Capas", fg="white", bg="gray", justify=CENTER)
        self.labelTitle.grid(row=0, column=0, padx=0, pady=5)
        self.labelTitle.config(width=15, font='Helvetica 10 bold')

        self.labelTitle = Label(self.panelBorder, text="N° de neuronas", fg="white", bg="gray", justify=CENTER)
        self.labelTitle.grid(row=0, column=1, padx=0, pady=5)
        self.labelTitle.config(width=25, font='Helvetica 10 bold')

        self.labelTitle = Label(self.panelBorder, text="Función de activación", fg="white", bg="gray", justify=CENTER)
        self.labelTitle.grid(row=0, column=2, padx=0, pady=5)
        self.labelTitle.config(width=25, font='Helvetica 10 bold')

        self.panelConfig = Label(self.panelBorder)
        self.panelConfig.grid(row=1, column=0, padx=0, pady=5, columnspan=3)
        self.panelConfig.config(width=300, height=30)

        self.panelSep = Label(self.panelConfig)
        self.panelSep.grid(row=0, column=0, padx=5, pady=0, columnspan=2)
        self.panelSep.config(width=25, height=0)

        for i in range(len(self.list_hidden_layers)):
            labelHiddenLayer = Label(self.panelConfig, text=f"Capa {i+1}", fg="blue", justify=CENTER)
            labelHiddenLayer.grid(row=i+1, column=0, padx=5, pady=5)
            labelHiddenLayer.config(width=15, font='Helvetica 10 bold')
            labelHidden = Label(self.panelConfig, text=f"{self.list_hidden_layers[i]}", fg="red", justify=CENTER)
            labelHidden.grid(row=i+1, column=1, padx=5, pady=5)
            labelHidden.config(width=25, font='Helvetica 10 bold')
            labelFunction = Label(self.panelConfig, text=f"{self.type_function(self.list_hidden_functions[i])}", fg="red", justify=CENTER)
            labelFunction.grid(row=i+1, column=2, padx=5, pady=5)
            labelFunction.config(width=25, font='Helvetica 8')

        labelHiddenLayer = Label(self.panelConfig, text="Capa de salida", fg="blue", justify=CENTER)
        labelHiddenLayer.grid(row=len(self.list_hidden_layers)+1, column=0, padx=5, pady=5)
        labelHiddenLayer.config(width=15, font='Helvetica 10 bold')
        labelHidden = Label(self.panelConfig, text=f"{self.salidas}", fg="red", justify=CENTER)
        labelHidden.grid(row=len(self.list_hidden_layers)+1, column=1, padx=5, pady=5)
        labelHidden.config(width=25, font='Helvetica 10 bold')
        labelFunction = Label(self.panelConfig, text=f"{self.type_function(self.list_hidden_functions[-1])}", fg="red", justify=CENTER)
        labelFunction.grid(row=len(self.list_hidden_layers)+1, column=2, padx=5, pady=5)
        labelFunction.config(width=25, font='Helvetica 8')
        panelSep = Label(self.panelConfig)
        panelSep.grid(row=len(self.list_hidden_layers)+2, column=0, padx=5, pady=0, columnspan=2)
        panelSep.config(width=25, height=0)

    def type_function(self, function_list):
        if function_list == 0:
            return 'Sigmoide'
        elif function_list == 1:
            return 'Tangente hiperbolica'
        elif function_list == 2:
            return 'Seno'
        elif function_list == 3:
            return 'Lineal'