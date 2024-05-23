from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import threading
import numpy as np
import pandas as pd
import csv
from rna_back import NeuralNetwork as rback
from rna import NeuralNetwork as rbackmc
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from window_msg import *
from w_umbral_weight import *
from w_config_net import *
from label_header import *
from panel_dataset import *
from panel_grafica_error import *
from panel_param_train import *
from panel_weight_umbral import *
from panel_predict import *
from save_report import *


class Window:

    def __init__(self, master):
        self.isOverflow = False
        self.isTrained = False
        self.isEntryExit = False
        self.isNumber = False
        self.list_hidden_layers = []
        self.list_hidden_functions = []
        self.u_w_input_init = [] 
        self.u_w_hidden_init = []
        self.u_w_output_init = []
        self.u_w_input_end = []
        self.u_w_hidden_end = []
        self.u_w_output_end = []
        self.root = master
        self.showWindow()
        self.createFrame()
        self.createControls()
        self.createMenuBar()
        self.root.mainloop()
        
    def showWindow(self):
        self.root.title("RNADelta ")
        self.root.resizable(0,0)
        self.root.iconbitmap("icono.ico")

    def createFrame(self):
        self.frame = Frame(self.root, width=850, height=550, pady=30, padx=20)
        self.frame.pack()

    def createMenuBar(self):
        self.menuBar = Menu(self.frame)
        self.itemModel = Menu(self.menuBar, tearoff=False)
        self.itemModel.add_command(label="Entrenar", command=self.trainModel)
        self.itemModel.add_command(label="Cargar dataset", command=self.charge_CSV)
        self.itemModel.add_command(label="Restablecer", command=self.reset)
        self.itemModel.add_command(label="Salir", command=self.root.quit)
        self.menuBar.add_cascade(menu=self.itemModel, label="Modelo")
        self.root.config(menu=self.menuBar)

    def createControls(self):
        self.txtEntradas = createLabelEntrada(self.frame)
        self.txtSalidas = createLabelSalida(self.frame)
        self.txtPatrones = createLabelPatrones(self.frame)
        self.panelDataset, self.text_areaS, self.text_areaE = createPanelDataset(self.frame, self.charge_CSV)
        self.panelGrafica = createPanelGraficaError(self.frame)
        self.createPanelSeparator()
        self.txtEpochs, self.txtError, self.txtRate, self.txtHidden = createPanelParamTrain(self, self.frame, self.trainModel)
        createPanelWeightAndUmbral(self.frame, self.getWeightEnd, self.getUmbralEnd, self.getWeightInit, self.getUmbralInit)
        self.createPanelResetAndShowConfig()
        self.panelPredict = createPanelPredict(self.frame)
        self.txtPredict = createGroupInputPredict(self.frame, self.panelPredict, self.predict)
        self.txtResult = createGroupInputResult(self.frame, self.panelPredict)

    def createPanelSeparator(self):
        self.panelSeparator = Label(self.frame)
        self.panelSeparator.grid(row=4, column=0, padx=5, pady=2, columnspan=6)
        self.panelSeparator.config(width=100, height=2)

    def createPanelResetAndShowConfig(self):
        self.panelBorder = Label(self.frame, bg="gray")
        self.panelBorder.grid(row=5, column=2, padx=1, pady=1, columnspan=2, rowspan=4)
        # BOTON PARA MOSTRAR LA CONFIGURACION DE LA RED
        self.panelBtnShowConfigLayers = Label(self.panelBorder, bg="gray")
        self.panelBtnShowConfigLayers.grid(row=0, column=0, padx=1, pady=2)
        self.btnconfigLayers = Button(self.panelBtnShowConfigLayers, text="Configuración de la red", command=self.showConfig)
        self.btnconfigLayers.grid(row=0, column=0)
        self.btnconfigLayers.config(padx=1, pady=4, width=25)
        self.btnconfigLayers.config(bg="green3", foreground="white", font='Helvetica 10 bold')
        # BOTON PARA RESTABLECER LA APLICACION
        self.panelBtnReset = Label(self.panelBorder, bg="gray")
        self.panelBtnReset.grid(row=1, column=0, padx=1, pady=2)
        self.btnReset = Button(self.panelBtnReset, text="Restablecer", command=self.reset)
        self.btnReset.grid(row=0, column=0)
        self.btnReset.config(padx=1, pady=4, width=25)
        self.btnReset.config(bg="blue3", foreground="white", font='Helvetica 10 bold')

    def charge_CSV(self):
        self.csv_filename = fd.askopenfilename(initialdir="/", title="Seleccione el archivo CSV", filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
        # Verificar si se seleccionó un archivo
        if self.csv_filename:
            # Leer el archivo CSV y obtener sus contenidos
            df = pd.read_csv(self.csv_filename)
            self.entradas = df.filter(regex='x').values
            self.salidas = df.filter(regex='yd').values
            if (self.entradas.size != 0) and (self.salidas.size != 0):
                # Mostrar los contenidos del archivo CSV en una ventana de texto
                self.showDataset()
                self.isEntryExit = True
            else:
                WindowMsg("Alerta", "El conjunto de datos no cumple con las condiciones de entrada")

    def showDataset(self):
        # Entradas
        self.text_areaE.delete(1.0, END)  # Limpiar el área de texto
        self.text_areaE.insert(END, self.entradas)  # Insertar los datos del CSV en el área de texto
        text = StringVar()
        text.set("")
        self.txtEntradas.delete(0, END)
        text.set(self.entradas.shape[1])
        self.txtEntradas.insert(INSERT, text.get())
        # Salidas 
        self.text_areaS.delete(1.0, END)  # Limpiar el área de texto
        self.text_areaS.insert(END, self.salidas)  # Insertar los datos del CSV en el área de texto
        text = StringVar()
        text.set("")
        self.txtSalidas.delete(0, END)
        text.set(self.salidas.shape[1])
        self.txtSalidas.insert(INSERT, text.get())
        self.txtPatrones.delete(0, END)
        text.set(self.entradas.shape[0])
        self.txtPatrones.insert(INSERT, text.get())

    def reciveData(self, hidden_layers, hidden_functions):
        self.list_hidden_layers = hidden_layers
        self.list_hidden_functions = hidden_functions

    def trainModel(self):
        progressbar = ttk.Progressbar(self.panelSeparator)
        progressbar.grid(row=0, column=0, padx=5, pady=5, columnspan=3)
        t = threading.Thread(target=self.train)
        t.start()
        self.schedule_check(t, progressbar)

    def schedule_check(self, t, progressbar):
        self.root.after(500, self.check_if_done, t, progressbar)

    def check_if_done(self, t, progressbar):
        if not t.is_alive():
            progressbar.destroy()
            if(self.isTrained):
                if(self.isOverflow):
                    WindowMsg("Alerta", "La red se han desbordado. \n Considere usar una tasa de aprendizaje menor (0.001)")
                else:
                    self.graficar()
            elif(not self.isEntryExit):
                WindowMsg("Alerta", "Debe cargar las entradas y salidas")
            elif(self.isNumber):
                WindowMsg("Alerta", "Los parámetros de entrenamiento deben ser numericos")
            else:
                WindowMsg("Alerta", "Debe ingresar todos los parámetros de entrenamiento")
        else:
            x = 10
            x += 10
            progressbar.step(x)
            self.schedule_check(t, progressbar)

    def train(self):
        try:
            textEntradas = self.text_areaE.get("1.0", "end-1c")
            textSalidas = self.text_areaS.get("1.0", "end-1c")
            textEpochs = self.txtEpochs.get()
            textError = self.txtError.get()
            textRate = self.txtRate.get()
            textHidden = self.txtHidden.get()

            if (textEntradas.strip()) and (textSalidas.strip()):
                if len(self.list_hidden_functions) and (textHidden.strip()) and (textEpochs.strip()) and (textError.strip()) and (textRate.strip()):
                    if len(self.list_hidden_layers):
                        self.epochs = int(self.txtEpochs.get())
                        self.tol = float(self.txtError.get())
                        self.learning_rate = float(self.txtRate.get())
                        X = self.entradas
                        y = self.salidas
                        # Parámetros de entrada
                        input_size = self.entradas.shape[1]
                        output_size = self.salidas.shape[1]
                        self.nnback = rback(input_size, self.list_hidden_layers, self.list_hidden_functions, output_size)
                        self.isOverflow, self.errors, self.iters, self.u_w_input_init, self.u_w_hidden_init, self.u_w_output_init, self.u_w_input_end, self.u_w_hidden_end, self.u_w_output_end = self.nnback.train(X, y, epochs=self.epochs, learning_rate=self.learning_rate, tol=self.tol)
                        saveResultTraining(self.entradas, self.salidas, self.epochs, self.tol, self.learning_rate, self.iters, self.u_w_input_end[0], self.u_w_input_end[1], self.u_w_output_end[0], self.u_w_output_end[1], 'BACKPROPAGATION')
                        self.isTrained = True
                    else:
                        self.epochs = int(self.txtEpochs.get())
                        self.tol = float(self.txtError.get())
                        self.learning_rate = float(self.txtRate.get())
                        X = self.entradas
                        y = self.salidas
                        # Parámetros de entrada
                        input_size = self.entradas.shape[1]
                        output_size = self.salidas.shape[1]
                        self.nnback = rbackmc(input_size, self.list_hidden_functions, output_size)
                        self.isOverflow, self.errors, self.iters, self.u_w_input_init, self.u_w_input_end = self.nnback.train(X, y, epochs=self.epochs, learning_rate=self.learning_rate, tol=self.tol)
                        saveResultTraining(self.entradas, self.salidas, self.epochs, self.tol, self.learning_rate, self.iters, self.u_w_input_end[0], self.u_w_input_end[1], self.u_w_input_init[0], self.u_w_input_init[1], 'BACKPROPAGATION')
                        self.isTrained = True
                else:
                    self.isTrained = False
            else:
                self.isEntryExit = False
        except ValueError:
            self.isNumber = True
            print(ValueError.args[0])

    def predict(self):
        try:
            textPredict = self.txtPredict.get()
            if(self.isTrained):
                entries = self.entradas.shape[1]
                if(textPredict.strip()):
                    if(len(textPredict.split(",")) == entries):
                        data = self.txtPredict.get()
                        data = data.split(",")
                        data = np.array(data, dtype=float)
                        prediction = self.nnback.forward([data])
                        prediction = np.around(prediction, decimals=1)
                        text = StringVar()
                        text.set("")
                        self.txtResult.delete(0, END)
                        text.set(prediction[0])
                        self.txtResult.insert(INSERT, text.get())
                    else:
                        WindowMsg("Alerta", "El número de entradas no coincide con los valores dados")
                else:
                    WindowMsg("Alerta", "Debe ingresar un valor a predecir")
            else:
                    WindowMsg("Alerta", "El modelo no ha sido entrenado")
        except ValueError:
            WindowMsg("Alerta", "Los valores deben ser numericos")  

    def getWeightEnd(self):
        if(len(self.list_hidden_layers)):
            WindowWeight(self.u_w_input_end[0], self.u_w_hidden_end[0], self.u_w_output_end[0])
        else:
            WindowWeight(self.u_w_input_end[0], [], [])

    def getUmbralEnd(self):
        if(len(self.list_hidden_layers)):
            WindowUmbral(self.u_w_input_end[1], self.u_w_hidden_end[1], self.u_w_output_end[1])  
        else:
            WindowUmbral(self.u_w_input_end[1], [], [])  

    def getWeightInit(self):
        if(len(self.list_hidden_layers)):
            WindowWeight(self.u_w_input_init[0], self.u_w_hidden_init[0], self.u_w_output_init[0])  
        else:
            WindowWeight(self.u_w_input_init[0], [], [])  

    def getUmbralInit(self):
        if(len(self.list_hidden_layers)):
            WindowUmbral(self.u_w_input_init[1], self.u_w_hidden_init[1], self.u_w_output_init[1]) 
        else:
            WindowUmbral(self.u_w_input_init[1], [], []) 

    def graficar(self):
        x = np.array(self.iters)
        y = np.array(self.errors)
        if np.min(y) > 1:
            y = y / 10
        fig = Figure(figsize=(5, 5), dpi=60)
        ax = fig.add_subplot(111)
        # Graficar los datos
        ax.plot(x, y, color='b', label='Error de la iteración', marker='o')  
        ax.axhline(y=self.tol, color='r', linestyle='--', label=f'Error máximo permitido ({self.txtError.get()})')
        ax.set_xlabel('Iteraciones')
        ax.set_ylabel('Error')
        ax.set_ylim(0, 1)
        ax.legend()
        canvas = FigureCanvasTkAgg(fig, master=self.panelGrafica)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, padx=1, pady=1)

    def showConfig(self):
        if self.isTrained:
            WindowConfigNet(self.epochs, self.learning_rate, self.tol, self.entradas.shape[1], self.salidas.shape[1], self.salidas.shape[0], self.list_hidden_layers, self.list_hidden_functions)
        else:
            WindowMsg("Alerta", "La red neuronal no ha sido configurada o entrenada")

    def reset(self):
        self.isOverflow = False
        self.isTrained = False
        self.isEntryExit = False
        self.isNumber = False
        self.list_hidden_layers = []
        self.list_hidden_functions = []
        self.u_w_input_init = [] 
        self.u_w_hidden_init = []
        self.u_w_output_init = []
        self.u_w_input_end = []
        self.u_w_hidden_end = []
        self.u_w_output_end = []
        self.frame.destroy()
        self.createFrame()
        self.createControls()
        self.createMenuBar()


if __name__ == "__main__":
    root = Tk()
    Window(root)
