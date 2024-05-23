from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from w_config_hidden_layers import *
from window_msg import *


def createPanelParamTrain(master, frame, trainModel):
    global txtHidden
    global rootFather
    global outputs

    rootFather = master

    panelBorder = Label(frame, bg="gray")
    panelBorder.grid(row=1, column=2, padx=5, pady=10, columnspan=2, rowspan=2)
    panelBorder.config(width=300, height=20)
    panelConfig = Label(panelBorder)
    panelConfig.grid(row=1, column=0, padx=5, pady=5)
    panelConfig.config(width=300, height=30)
    panelSep = Label(panelConfig)
    panelSep.grid(row=0, column=0, padx=5, pady=0, columnspan=2)
    panelSep.config(width=25, height=0)
    panelParamTrain = Label(panelBorder)
    panelParamTrain.grid(row=3, column=0, padx=5, pady=5)
    panelParamTrain.config(width=300, height=30)
    labelTitle = Label(panelBorder, text="Parámetros de entrenamiento", fg="white", bg="gray")
    labelTitle.grid(row=0, column=0)
    labelTitle.config(width=25, font='Helvetica 10 bold')
    panelSep = Label(panelParamTrain)
    panelSep.grid(row=0, column=0, padx=5, pady=0, columnspan=2)
    panelSep.config(width=25, height=0)
    # NUMERO DE CAPAS OCULTAS
    labelHidden = Label(panelConfig, text="N° de capas ocultas", fg="blue", justify=LEFT)
    labelHidden.grid(row=1, column=0, padx=10, pady=2)
    labelHidden.config(width=19, font='Helvetica 10 bold')
    txtHidden = Entry(panelConfig, fg="red", justify=CENTER)
    txtHidden.grid(row=1, column=1, padx=10, pady=2)
    txtHidden.config(width=15, font='Helvetica 10 bold')
    panelSep = Label(panelConfig)
    panelSep.grid(row=2, column=0, padx=5, pady=0, columnspan=2)
    panelSep.config(width=25, height=0)
    # BOTON DE CONFIGURACION DE LAS CAPAS OCULTAS
    panelBtnConf = Label(panelBorder, bg="gray")
    panelBtnConf.grid(row=2, column=0, padx=2, pady=0)
    panelBtnConf.config(width=300, height=5)
    btnConf = Button(panelBtnConf, text="Configurar capas", command=showConfigWind)
    btnConf.grid(row=0, column=0, columnspan=2)
    btnConf.config(padx=10, pady=4, width=35)
    btnConf.config(bg="green3", foreground="white", font='Helvetica 10 bold')
    # NUMERO DE ITERACIONES
    labelEpochs = Label(panelParamTrain, text="N° de iteraciones", fg="blue", justify=LEFT)
    labelEpochs.grid(row=3, column=0, padx=10, pady=5)
    labelEpochs.config(width=19, font='Helvetica 10 bold')
    txtEpochs = Entry(panelParamTrain, fg="red", justify=CENTER)
    txtEpochs.grid(row=3, column=1, padx=10, pady=3)
    txtEpochs.config(width=15, font='Helvetica 10 bold')
    # ERROR MAXIMO PERMITIDO
    labelError = Label(panelParamTrain, text="Error máximo", fg="blue", justify=LEFT)
    labelError.grid(row=4, column=0, padx=10, pady=5)
    labelError.config(width=19, font='Helvetica 10 bold')
    txtError = Entry(panelParamTrain, fg="red", justify=CENTER)
    txtError.grid(row=4, column=1, padx=10, pady=3)
    txtError.config(width=15, font='Helvetica 10 bold')
    # RATA DE APRENDIZAJE
    labelRate = Label(panelParamTrain, text="Rata de aprendizaje", fg="blue", justify=LEFT)
    labelRate.grid(row=5, column=0, padx=10, pady=5)
    labelRate.config(width=19, font='Helvetica 10 bold')
    txtRate = Entry(panelParamTrain, fg="red", justify=CENTER)
    txtRate.grid(row=5, column=1, padx=10, pady=3)
    txtRate.config(width=15, font='Helvetica 10 bold')
    panelSep = Label(panelParamTrain)
    panelSep.grid(row=6, column=0, padx=5, pady=0, columnspan=2)
    panelSep.config(width=25, height=0)
    # BOTON PARA ENTRENAL EL MODELO
    panelBtnTrain = Label(panelBorder, bg="gray")
    panelBtnTrain.grid(row=4, column=0, padx=2, pady=0)
    panelBtnTrain.config(width=300, height=5)
    btnTrain = Button(panelBtnTrain, text="Entrenar modelo", command=trainModel)
    btnTrain.grid(row=0, column=0, columnspan=2)
    btnTrain.config(padx=10, pady=4, width=35)
    btnTrain.config(bg="green3", foreground="white", font='Helvetica 10 bold')
    return txtEpochs, txtError, txtRate, txtHidden


def showConfigWind():
    textHidden = txtHidden.get()
    if (rootFather.isEntryExit):
        if (textHidden.strip()):
            hidden_size = int(txtHidden.get())
            WindowConfigHidden(rootFather, hidden_size)
        else:
            WindowMsg("Alerta", "Debe ingresar la cantidad de capas ocultas")
    else:
        WindowMsg("Alerta", "Debe cargar las entradas y salidas")