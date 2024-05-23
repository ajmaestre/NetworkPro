
from tkinter import *
from tkinter import filedialog as fd
from logic import *
from tkinter import ttk
import threading



letters = []
letters_ = []
textPredicted = []
global frame
global root


def showWindow():
    root.title("ROChar ")
    root.resizable(0,0)
    root.iconbitmap("images/DATA/icono.ico")


def createFrame():
    frame = Frame(root, width=850, height=550, pady=20, padx=10)
    frame.pack()
    return frame


def createMenuBar():
    menuBar = Menu(frame)
    itemModel = Menu(menuBar, tearoff=False)
    itemModel.add_command(label="Entrenar", command=trainModel)
    itemModel.add_command(label="Salir", command=root.quit)
    menuBar.add_cascade(menu=itemModel, label="Modelo")
    root.config(menu=menuBar)


def createControls():
    global panelImage
    global panel
    global txtResult
    global txtAccuracy
    labelAccuracy = Label(frame, text="Precisión", fg="blue")
    labelAccuracy.grid(row=0, column=0, padx=5, pady=15)
    labelAccuracy.config(width=10, font='Helvetica 14 bold')
    txtAccuracy = Entry(frame, fg="red", justify=CENTER)
    txtAccuracy.grid(row=0, column=1, padx=5, pady=15)
    txtAccuracy.config(width=10, font='Helvetica 14 bold')
    panelImage = PhotoImage(file="images/DATA/bg-1.png")
    panel = Label(frame, image=panelImage)
    panel.grid(row=1, column=0, padx=5, pady=5, columnspan=2)
    panel.config(width=300, height=200)
    txtResult = Entry(frame, justify=CENTER)
    txtResult.grid(row=2, column=0, padx=5, pady=20, columnspan=2)
    txtResult.config(width=15, font='Arial 25 bold')
    btnInsert = Button(frame, text="Insertar", command=chargeImage)
    btnInsert.grid(row=3, column=0)
    btnInsert.config(padx=10, pady=5, width=10)
    btnInsert.config(bg="green3", foreground="white", font='Helvetica 12 bold')
    btnConvert = Button(frame, text="Predecir", command=convertLetter)
    btnConvert.grid(row=3, column=1)
    btnConvert.config(padx=10, pady=5, width=10)
    btnConvert.config(bg="blue2", foreground="white", font='Helvetica 12 bold')


def chargeImage():
    global images
    global img
    img = fd.askopenfilename(initialdir = "/", title= "Seleccione el archivo", filetypes=(("png files","*.png"),("all files","*.*")))
    images = PhotoImage(file=img)
    labelImage = Label(panel, image=images)
    labelImage.grid(row=0, column=0, padx=25, pady=25)
    labelImage.config(width=250, height=150)


def convert():
    textPredicted = []
    textPredicted = load_manuscrito(img)
    text = str()
    for i in range(0, len(textPredicted)):
        text += textPredicted[i]
    txtResult.insert(INSERT, text)


def convertLetter():
    text = StringVar()
    text.set("")
    txtResult.delete(0, END)
    text.set(load_letter(img))
    txtResult.insert(INSERT, text.get())


def trainModel():
    progressbar = ttk.Progressbar(panel)
    progressbar.grid(row=1, column=0, padx=100, pady=90)
    t = threading.Thread(target=trained)
    t.start()
    schedule_check(t, progressbar)


def schedule_check(t, progressbar):
    root.after(1000, check_if_done, t, progressbar)


def check_if_done(t, progressbar):
    if not t.is_alive():
        progressbar.destroy()
    else:
        x = 10
        x += 10
        progressbar.step(x)
        schedule_check(t, progressbar)


def trained():
    create_dataset(letters_, letters)
    text = StringVar()
    text.set("")
    txtAccuracy.delete(0, END)
    text.set(train_model())
    txtAccuracy.insert(INSERT, text.get())


if __name__ == "__main__":
    root = Tk()
    showWindow()
    frame = createFrame()
    createControls()
    createMenuBar()
    root.mainloop()
