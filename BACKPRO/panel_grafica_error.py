from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def createPanelGraficaError(frame):
    panelBorder = Label(frame, bg="gray")
    panelBorder.grid(row=1, column=4, padx=5, pady=10, rowspan=2, columnspan=2)
    panelBorder.config(width=350, height=250)
    labelTitle = Label(panelBorder, text="Gráfica de entrenamiento", fg="white", bg="gray")
    labelTitle.grid(row=0, column=0)
    labelTitle.config(width=20, font='Helvetica 10 bold')
    panelGrafica = Label(panelBorder, bg="gray")
    panelGrafica.grid(row=1, column=0, padx=2, pady=2)
    panelGrafica.config(width=350, height=250)
    fig = Figure(figsize=(5, 5), dpi=60)
    ax = fig.add_subplot(111)
    ax.axhline(y=0.2, color='r', linestyle='--', label='Error máximo permitido')
    ax.set_xlabel('Iteraciones')
    ax.set_ylabel('Error')
    ax.set_ylim(0, 1)
    ax.legend()
    canvas = FigureCanvasTkAgg(fig, master=panelGrafica)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, padx=1, pady=1)
    return panelGrafica