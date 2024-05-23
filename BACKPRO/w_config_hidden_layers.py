from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from window_msg import *


class WindowConfigHidden:

    def __init__(self, rootFather, size):
        self.master = rootFather
        self.root = Tk()
        self.showWindow()
        self.createFrame()
        self.createControls(size)
        self.root.mainloop()

    def showWindow(self):
        self.root.title("RNADelta ")
        self.root.resizable(0,0)
        self.root.iconbitmap("icono.ico")

    def createFrame(self):
        self.frame = Frame(self.root, pady=20, padx=11)
        self.frame.pack()

    def createControls(self, size):
        self.size_layer = size
        self.list_combo = []
        self.list_text = []

        self.panelBorder = Label(self.frame, bg="gray")
        self.panelBorder.grid(row=1, column=2, padx=0, pady=10, columnspan=2, rowspan=2)
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

        for i in range(size):
            labelHiddenLayer = Label(self.panelConfig, text=f"Capa {i+1}", fg="blue", justify=CENTER)
            labelHiddenLayer.grid(row=i+1, column=0, padx=5, pady=5)
            labelHiddenLayer.config(width=15, font='Helvetica 10 bold')
            txtHidden = Entry(self.panelConfig, fg="red", justify=CENTER)
            txtHidden.grid(row=i+1, column=1, padx=5, pady=5)
            txtHidden.config(width=25, font='Helvetica 10 bold')
            combobox = ttk.Combobox(self.panelConfig, values=["Sigmoide", "Tangente hiperbolica", "Seno"], justify=CENTER)
            combobox.grid(row=i+1, column=2, padx=5, pady=5)
            combobox.config(width=25, font='Helvetica 8')
            self.list_combo.append(combobox)
            self.list_text.append(txtHidden)

        labelHiddenLayer = Label(self.panelConfig, text="Capa de salida", fg="blue", justify=CENTER)
        labelHiddenLayer.grid(row=size+1, column=0, padx=5, pady=5)
        labelHiddenLayer.config(width=15, font='Helvetica 10 bold')
        labelHidden = Label(self.panelConfig, text=f"{self.master.salidas.shape[1]}", fg="red", justify=CENTER)
        labelHidden.grid(row=size+1, column=1, padx=5, pady=5)
        labelHidden.config(width=25, font='Helvetica 10 bold')
        combobox = ttk.Combobox(self.panelConfig, values=["Sigmoide", "Tangente hiperbolica", "Seno", "Lineal"], justify=CENTER)
        combobox.grid(row=size+1, column=2, padx=5, pady=5)
        combobox.config(width=25, font='Helvetica 8')
        panelSep = Label(self.panelConfig)
        panelSep.grid(row=size+2, column=0, padx=5, pady=0, columnspan=2)
        panelSep.config(width=25, height=0)
        self.list_combo.append(combobox)

        self.panelBtnSave = Label(self.panelBorder, bg="gray")
        self.panelBtnSave.grid(row=2, column=0, padx=2, pady=5, columnspan=3)
        self.panelBtnSave.config(width=300, height=5)
        self.btnCancel = Button(self.panelBtnSave, text="Cancelar", command=self.cancel)
        self.btnCancel.grid(row=0, column=0)
        self.btnCancel.config(padx=0, pady=4, width=32)
        self.btnCancel.config(bg="green3", foreground="white", font='Helvetica 10 bold')
        self.btnSave = Button(self.panelBtnSave, text="Registrar", command=self.save)
        self.btnSave.grid(row=0, column=2)
        self.btnSave.config(padx=0, pady=4, width=30)
        self.btnSave.config(bg="green3", foreground="white", font='Helvetica 10 bold')

    def type_function(self, function_list):
        if function_list == 'Sigmoide':
            return 0
        elif function_list == 'Tangente hiperbolica':
            return 1
        elif function_list == 'Seno':
            return 2
        elif function_list == 'Lineal':
            return 3

    def save(self):
        try:
            self.hidden_layers = []
            self.hidden_functions = []
            self.is_saved = True
            for i in range(self.size_layer):
                textHidden = self.list_text[i].get()
                comboFunction = self.list_combo[i].get()
                if (textHidden.strip()) and (comboFunction.strip()):
                    hidden_layer = int(self.list_text[i].get())
                    hidden_function = self.type_function(self.list_combo[i].get())
                    self.hidden_layers.append(hidden_layer)
                    self.hidden_functions.append(hidden_function)
                else:
                    self.hidden_layers = []
                    self.hidden_functions = []
                    self.is_saved = False
                    break
            comboFunction = self.list_combo[-1].get()
            if (comboFunction.strip()):
                hidden_function = self.type_function(self.list_combo[-1].get())
                self.hidden_functions.append(hidden_function)
            else:
                self.hidden_layers = []
                self.hidden_functions = []
                self.is_saved = False
            if self.is_saved:
                self.master.reciveData(self.hidden_layers, self.hidden_functions)
                self.root.destroy()
            else:
                WindowMsg("Alerta", "Debe ingresar todos los parámetros")
        except ValueError:
            WindowMsg("Alerta", "Los valores de las capas deben ser numericos")  

    def cancel(self):
        self.root.destroy()
