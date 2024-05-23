from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import threading
import numpy as np
import csv
from rna import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from window_msg import *
import datetime


def showWindow():
    root.title("RNADelta ")
    root.resizable(0,0)
    root.iconbitmap("icono.ico")


def createFrame():
    global frame
    frame = Frame(root, width=850, height=550, pady=30, padx=20)
    frame.pack()


def createMenuBar():
    menuBar = Menu(frame)
    itemModel = Menu(menuBar, tearoff=False)
    itemModel.add_command(label="Entrenar", command=trainModel)
    itemModel.add_command(label="Cargar entradas", command=chargeE_CSV)
    itemModel.add_command(label="Cargar salidas", command=chargeS_CSV)
    itemModel.add_command(label="Restablecer", command=reset)
    itemModel.add_command(label="Salir", command=root.quit)
    menuBar.add_cascade(menu=itemModel, label="Modelo")
    root.config(menu=menuBar)


def createControls():
    global panelImage
    panelImage = PhotoImage(file="bg-1.png")
    createLabelEntrada()
    createLabelSalida()
    createLabelPatrones()
    createPanelEntradas()
    createPanelSalidas()
    createPanelGraficaError()
    createPanelWeight()
    createPanelUmbral()
    createPanelSeparator()
    createPanelParamTrain()
    createPanelPredict()
    createGroupInputPredict()
    createGroupInputResult()

def createLabelEntrada():
    global txtEntradas
    labelEntradas = Label(frame, text="N° Entradas", fg="blue")
    labelEntradas.grid(row=0, column=0, padx=5, pady=5)
    labelEntradas.config(width=10, font='Helvetica 12 bold')
    txtEntradas = Entry(frame, fg="red", justify=CENTER)
    txtEntradas.grid(row=0, column=1, padx=5, pady=5)
    txtEntradas.config(width=10, font='Helvetica 12 bold')

def createLabelSalida():
    global txtSalidas
    labelSalidas = Label(frame, text="N° Salidas", fg="blue")
    labelSalidas.grid(row=0, column=2, padx=5, pady=5)
    labelSalidas.config(width=10, font='Helvetica 12 bold')
    txtSalidas = Entry(frame, fg="red", justify=CENTER)
    txtSalidas.grid(row=0, column=3, padx=5, pady=5)
    txtSalidas.config(width=10, font='Helvetica 12 bold')

def createLabelPatrones():
    global txtPatrones
    labelPatrones = Label(frame, text="N° Patrones", fg="blue")
    labelPatrones.grid(row=0, column=4, padx=5, pady=5)
    labelPatrones.config(width=10, font='Helvetica 12 bold')
    txtPatrones = Entry(frame, fg="red", justify=CENTER)
    txtPatrones.grid(row=0, column=5, padx=5, pady=5)
    txtPatrones.config(width=10, font='Helvetica 12 bold')

def createPanelEntradas():
    global panelEntradas
    global text_areaE
    panelEntradas = Label(frame, image=panelImage)
    panelEntradas.grid(row=1, column=0, padx=5, pady=5, rowspan=2)
    panelEntradas.config(width=150, height=200)
    text_areaE = Text(panelEntradas)
    text_areaE.delete(1.0, END)  # Limpiar el área de texto
    text_areaE.grid(row=0, column=0, padx=5, pady=5)
    text_areaE.config(width=20, height=16)
    # BOTOB CARGAR ENTRADAS
    btnInsertE = Button(panelEntradas, text="Cargar Entradas", command=chargeE_CSV)
    btnInsertE.grid(row=1, column=0)
    btnInsertE.config(padx=20, pady=3, width=15)
    btnInsertE.config(bg="green3", foreground="white", font='Helvetica 10 bold')

def createPanelSalidas():
    global panelSalidas
    global text_areaS
    panelSalidas= Label(frame, image=panelImage)
    panelSalidas.grid(row=1, column=1, padx=5, pady=5, rowspan=2)
    panelSalidas.config(width=150, height=200)
    text_areaS = Text(panelSalidas)
    text_areaS.delete(1.0, END)  # Limpiar el área de texto
    text_areaS.grid(row=0, column=0, padx=5, pady=5)
    text_areaS.config(width=20, height=16)
    # BOTON CARGAR SALIDAS
    btnInsertS = Button(panelSalidas, text="Cargar Salidas", command=chargeS_CSV)
    btnInsertS.grid(row=1, column=0)
    btnInsertS.config(padx=20, pady=3, width=15)
    btnInsertS.config(bg="green3", foreground="white", font='Helvetica 10 bold')

def createPanelGraficaError():
    global panelGrafica
    panelBorder = Label(frame, bg="gray")
    panelBorder.grid(row=1, column=4, padx=1, pady=1, rowspan=2, columnspan=2)
    panelBorder.config(width=350, height=250)
    labelTitle = Label(panelBorder, text="Gráfica de entrenamiento", fg="white", bg="gray")
    labelTitle.grid(row=0, column=0)
    labelTitle.config(width=20, font='Helvetica 10 bold')
    panelGrafica = Label(panelBorder, bg="gray")
    panelGrafica.grid(row=1, column=0, padx=1, pady=1)
    panelGrafica.config(width=350, height=250)
    fig = Figure(figsize=(5, 5), dpi=55)
    ax = fig.add_subplot(111)
    ax.axhline(y=0.2, color='r', linestyle='--', label='Error máximo permitido')
    ax.set_xlabel('Iteraciones')
    ax.set_ylabel('Error')
    ax.set_ylim(0, 1)
    ax.legend()
    canvas = FigureCanvasTkAgg(fig, master=panelGrafica)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, padx=1, pady=1)

def createPanelUmbral():
    global panelUmbral
    global panelUmbralInit
    global text_areaU
    global text_areaUInit
    panelUmbralInit = Label(frame, bg="gray")
    panelUmbralInit.grid(row=1, column=2, padx=5, pady=5)
    panelUmbralInit.config(width=150, height=120)
    panelUmbral = Label(frame, bg="gray")
    panelUmbral.grid(row=2, column=2, padx=5, pady=5)
    panelUmbral.config(width=150, height=120)  
    labelUmbral = Label(panelUmbral, text="Umbral final", fg="white", bg="gray")
    labelUmbral.grid(row=0, column=0)
    labelUmbral.config(width=10, font='Helvetica 10 bold')
    text_areaU = Text(panelUmbral)
    text_areaU.delete(1.0, END)  # Limpiar el área de texto
    text_areaU.grid(row=1, column=0, padx=5, pady=5)
    text_areaU.config(width=20, height=7)
    labelUmbral = Label(panelUmbralInit, text="Umbral inicial", fg="white", bg="gray")
    labelUmbral.grid(row=0, column=0)
    labelUmbral.config(width=12, font='Helvetica 10 bold')
    text_areaUInit = Text(panelUmbralInit)
    text_areaUInit.delete(1.0, END)  # Limpiar el área de texto
    text_areaUInit.grid(row=1, column=0, padx=5, pady=5)
    text_areaUInit.config(width=20, height=7)

def createPanelWeight():
    global panelWeight
    global panelWeightInit
    global text_areaW
    global text_areaWInit
    panelWeightInit = Label(frame, bg="gray")
    panelWeightInit.grid(row=1, column=3, padx=5, pady=5)
    panelWeightInit.config(width=150, height=120)
    panelWeight = Label(frame, bg="gray")
    panelWeight.grid(row=2, column=3, padx=5, pady=5)
    panelWeight.config(width=150, height=120)
    labelWeight = Label(panelWeight, text="Peso final", fg="white", bg="gray")
    labelWeight.grid(row=0, column=0)
    labelWeight.config(width=10, font='Helvetica 10 bold')
    text_areaW = Text(panelWeight)
    text_areaW.delete(1.0, END)  # Limpiar el área de texto
    text_areaW.grid(row=1, column=0, padx=5, pady=5)
    text_areaW.config(width=20, height=7)
    labelWeight = Label(panelWeightInit, text="Peso inicial", fg="white", bg="gray")
    labelWeight.grid(row=0, column=0)
    labelWeight.config(width=10, font='Helvetica 10 bold')
    text_areaWInit = Text(panelWeightInit)
    text_areaWInit.delete(1.0, END)  # Limpiar el área de texto
    text_areaWInit.grid(row=1, column=0, padx=5, pady=5)
    text_areaWInit.config(width=20, height=7)

def createPanelSeparator():
    global panelSeparator
    panelSeparator = Label(frame)
    panelSeparator.grid(row=4, column=0, padx=5, pady=5, columnspan=6)
    panelSeparator.config(width=100, height=2)

def createPanelParamTrain():
    global txtEpochs
    global txtError
    global txtRate
    panelBorder = Label(frame, image=panelImage)
    panelBorder.grid(row=5, column=0, padx=1, pady=1, columnspan=3, rowspan=2)
    panelBorder.config(width=300, height=20)
    panelParamTrain = Label(panelBorder)
    panelParamTrain.grid(row=0, column=0, padx=5, pady=5)
    panelParamTrain.config(width=300, height=20)
    # NUMERO DE ITERACIONES
    labelEpochs = Label(panelParamTrain, text="N° de iteraciones", fg="blue")
    labelEpochs.grid(row=0, column=0, padx=10, pady=10)
    labelEpochs.config(width=15, font='Helvetica 11 bold')
    txtEpochs = Entry(panelParamTrain, fg="red", justify=CENTER)
    txtEpochs.grid(row=0, column=1, padx=10, pady=5)
    txtEpochs.config(width=10, font='Helvetica 11 bold')
    # ERROR MAXIMO PERMITIDO
    labelError = Label(panelParamTrain, text="Error máximo", fg="blue")
    labelError.grid(row=0, column=2, padx=10, pady=10)
    labelError.config(width=15, font='Helvetica 11 bold')
    txtError = Entry(panelParamTrain, fg="red", justify=CENTER)
    txtError.grid(row=0, column=3, padx=10, pady=10)
    txtError.config(width=10, font='Helvetica 11 bold')
    # RATA DE APRENDIZAJE
    labelRate = Label(panelParamTrain, text="Rata de aprendizaje", fg="blue")
    labelRate.grid(row=1, column=0, padx=10, pady=10)
    labelRate.config(width=15, font='Helvetica 11 bold')
    txtRate = Entry(panelParamTrain, fg="red", justify=CENTER)
    txtRate.grid(row=1, column=1, padx=10, pady=10)
    txtRate.config(width=10, font='Helvetica 11 bold')
    # BOTON PARA ENTRENAL EL MODELO
    btnTrain = Button(panelParamTrain, text="Entrenar modelo", command=trainModel)
    btnTrain.grid(row=1, column=2, columnspan=2)
    btnTrain.config(padx=10, pady=3, width=25)
    btnTrain.config(bg="green3", foreground="white", font='Helvetica 10 bold')

def createPanelPredict():
    global panelPredict
    panelBorder = Label(frame, image=panelImage)
    panelBorder.grid(row=5, column=3, padx=1, pady=1, columnspan=3, rowspan=4)
    panelBorder.config(width=300, height=20)
    panelPredict = Label(panelBorder)
    panelPredict.grid(row=0, column=0, padx=5, pady=5)
    panelPredict.config(width=300, height=20)

def createGroupInputPredict():
    global txtPredict
    txtPredict = Entry(panelPredict, fg="red", justify=CENTER)
    txtPredict.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
    txtPredict.config(width=35, font='Helvetica 11 bold')
    btnPredict = Button(panelPredict, text="Predecir", command=predict)
    btnPredict.grid(row=0, column=2)
    btnPredict.config(padx=15, pady=3, width=10)
    btnPredict.config(bg="green3", foreground="white", font='Helvetica 10 bold')

def createGroupInputResult():
    global txtResult
    labelResult = Label(panelPredict, text="Predicción", fg="blue")
    labelResult.grid(row=1, column=0, padx=5, pady=10)
    labelResult.config(width=15, font='Helvetica 11 bold')
    txtResult = Entry(panelPredict, fg="red", justify=CENTER)
    txtResult.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
    txtResult.config(width=35, font='Helvetica 11 bold')

def chargeS_CSV():
    global csv_filename
    global salidas
    csv_filename = fd.askopenfilename(initialdir="/", title="Seleccione el archivo CSV", filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
    # Verificar si se seleccionó un archivo
    if csv_filename:
        # Leer el archivo CSV y obtener sus contenidos
        with open(csv_filename, 'r') as file:
            csv_reader = csv.reader(file)
            csv_data = list(csv_reader)
        salidas = np.array(csv_data, dtype=np.int32)
        # Mostrar los contenidos del archivo CSV en una ventana de texto
        text_areaS.delete(1.0, END)  # Limpiar el área de texto
        text_areaS.insert(END, salidas)  # Insertar los datos del CSV en el área de texto
        text = StringVar()
        text.set("")
        txtSalidas.delete(0, END)
        text.set(salidas.shape[1])
        txtSalidas.insert(INSERT, text.get())
        txtPatrones.delete(0, END)
        text.set(entradas.shape[0])
        txtPatrones.insert(INSERT, text.get())

def chargeE_CSV():
    global csv_filename
    global entradas
    csv_filename = fd.askopenfilename(initialdir="/", title="Seleccione el archivo CSV", filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
    # Verificar si se seleccionó un archivo
    if csv_filename:
        # Leer el archivo CSV y obtener sus contenidos
        with open(csv_filename, 'r') as file:
            csv_reader = csv.reader(file)
            csv_data = list(csv_reader)
        entradas = np.array(csv_data, dtype=np.int32)
        # Mostrar los contenidos del archivo CSV en una ventana de texto
        text_areaE.delete(1.0, END)  # Limpiar el área de texto
        text_areaE.insert(END, entradas)  # Insertar los datos del CSV en el área de texto
        text = StringVar()
        text.set("")
        txtEntradas.delete(0, END)
        text.set(entradas.shape[1])
        txtEntradas.insert(INSERT, text.get())

def trainModel():
    progressbar = ttk.Progressbar(panelSeparator)
    progressbar.grid(row=0, column=0, padx=5, pady=5, columnspan=3)
    t = threading.Thread(target=train)
    t.start()
    schedule_check(t, progressbar)

def schedule_check(t, progressbar):
    root.after(500, check_if_done, t, progressbar)

def check_if_done(t, progressbar):
    if not t.is_alive():
        progressbar.destroy()
        if(resultTrain == 1):
            graficar()
            getWeightAndUmbral()
        elif(resultTrain == 0):
            createWind("Alerta", "Debe cargar las entradas y salidas")
        elif(resultTrain == 2):
            createWind("Alerta", "Los parámetros de entrenamiento deben ser numericos")
        else:
            createWind("Alerta", "Debe ingresar todos los parámetros de entrenamiento")
    else:
        x = 10
        x += 10
        progressbar.step(x)
        schedule_check(t, progressbar)

def train():
    global epochs
    global errors
    global weights
    global umbrals
    global weightsInit
    global umbralsInit
    global iters
    global tol
    global learning_rate
    global nn
    global resultTrain
    # Banco de datos
    try:
        textEntradas = text_areaE.get("1.0", "end-1c")
        textSalidas = text_areaS.get("1.0", "end-1c")
        textEpochs = txtEpochs.get()
        textError = txtError.get()
        textRate = txtRate.get()
        if (textEntradas.strip()) and (textSalidas.strip()):
            if (textEpochs.strip()) and (textError.strip()) and (textRate.strip()):
                epochs = int(txtEpochs.get())
                tol = float(txtError.get())
                learning_rate = float(txtRate.get())
                X = entradas
                y = salidas
                # Parámetros de entrada
                input_size = entradas.shape[1]
                output_size = salidas.shape[1]
                nn = NeuralNetwork(input_size, output_size)
                errors, iters, weights, umbrals, weightsInit, umbralsInit = nn.train(X, y, epochs=epochs, learning_rate=learning_rate, tol=tol)
                saveResultTraining(errors, iters, weights, umbrals, weightsInit, umbralsInit)
                resultTrain = 1
            else:
                resultTrain = -1
        else:
            resultTrain = 0
    except ValueError:
        resultTrain = 2

def saveResultTraining(errors, iters, weights, umbrals, weightsInit, umbralsInit):
    fileReport = np.array(["--------------------------------------------------------------------------------------"])
    header = "--------------------------------------------------------------------------------------"
    fecha_hora_actual = datetime.datetime.now()
    fecha_hora_actual = fecha_hora_actual.strftime('%Y-%m-%d-%H-%M-%S')
    title = f"Reporte de entrenamiento - {fecha_hora_actual}"
    fileReport = np.append(fileReport, title)
    fileReport = np.append(fileReport, "--------------------------------------------------------------------------------------")
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Numero de entradas")
    fileReport = np.append(fileReport, entradas.shape[1])
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Numero de salidas")
    fileReport = np.append(fileReport, salidas.shape[1])
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Numero de patrones")
    fileReport = np.append(fileReport, entradas.shape[0])
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Pesos iniciales")
    fileReport = np.append(fileReport, np.around(weightsInit, decimals=2))
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Umbrales iniciales")
    fileReport = np.append(fileReport, np.around(umbralsInit, decimals=2))
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Pesos finales")
    fileReport = np.append(fileReport, np.around(weights, decimals=2))
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Umbrales finales")
    fileReport = np.append(fileReport, np.around(umbrals, decimals=2))
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Iteraciones alcanzadas")
    fileReport = np.append(fileReport, iters[-1])
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Iteraciones totales")
    fileReport = np.append(fileReport, txtEpochs.get())
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Error maximo permitido")
    fileReport = np.append(fileReport, txtError.get())
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Rata de aprendizaje")
    fileReport = np.append(fileReport, txtRate.get())
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "--------------------------------------------------------------------------------------")
    fileReport = np.append(fileReport, f'Fecha de registo {fecha_hora_actual}')
    np.savetxt(f'report/report_{fecha_hora_actual}.txt', fileReport, fmt='%s', delimiter=',', header=header, footer=header)

def predict():
    try:
        isUmbral = text_areaU.get("1.0", "end-1c")
        isWeight = text_areaW.get("1.0", "end-1c")
        textPredict = txtPredict.get()
        if(isUmbral.strip()) and (isWeight.strip()):
            entries = entradas.shape[1]
            if(textPredict.strip()):
                if(len(textPredict) == entries):
                    data = txtPredict.get()
                    int(data)
                    data = np.array(list(data), dtype=int)
                    prediction = nn.forward([data])
                    text = StringVar()
                    text.set("")
                    txtResult.delete(0, END)
                    text.set(prediction[0])
                    txtResult.insert(INSERT, text.get())
                else:
                    createWind("Alerta", "El número de entradas no coincide con los valores dados")
            else:
                createWind("Alerta", "Debe ingresar un valor a predecir")
        else:
                createWind("Alerta", "El modelo no ha sido entrenado")
    except ValueError:
        createWind("Alerta", "Los valores deben ser numericos")

def getWeightAndUmbral():
    text_areaW.delete(1.0, END)  # Limpiar el área de texto
    text_areaW.insert(END, np.around(weights, decimals=2))  # Insertar los datos del CSV en el área de texto
    text_areaU.delete(1.0, END)  
    text_areaU.insert(END, np.around(umbrals.T, decimals=3))  
    text_areaWInit.delete(1.0, END)  
    text_areaWInit.insert(END, np.around(weightsInit, decimals=2))  
    text_areaUInit.delete(1.0, END)  
    text_areaUInit.insert(END, np.around(umbralsInit.T, decimals=3)) 

def graficar():
    x = iters
    y = errors
    fig = Figure(figsize=(5, 5), dpi=55)
    ax = fig.add_subplot(111)
    # Graficar los datos
    ax.plot(x, y, color='b', label='Error de la iteración', marker='o')  
    ax.axhline(y=tol, color='r', linestyle='--', label=f'Error máximo permitido ({txtError.get()})')
    ax.set_xlabel('Iteraciones')
    ax.set_ylabel('Error')
    ax.set_ylim(0, 1)
    ax.legend()
    canvas = FigureCanvasTkAgg(fig, master=panelGrafica)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, padx=1, pady=1)

def reset():
    frame.destroy()
    createFrame()
    createControls()
    createMenuBar()


if __name__ == "__main__":
    global root
    root = Tk()
    showWindow()
    createFrame()
    createControls()
    createMenuBar()
    root.mainloop()
