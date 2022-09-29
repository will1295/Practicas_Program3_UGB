#import PIL
from PIL import Image, ImageTk, ImageFilter
from tkinter import Tk, Button, Label, filedialog


def mostrar():
    imagen1 = Image.open(r"C:\Users\WilliamMon\Documents\Practicas_Program3_UGB\Semana11\lenguaje.jpg")
    #imagen1.show()
    imagen1resiz = imagen1.resize((200,200), Image.Resampling.LANCZOS)
    render1 = ImageTk.PhotoImage(imagen1resiz)    
    lbl1.configure(image=render1)
    lbl1.image = render1


def cargar():
    archivo = filedialog.askopenfilename()
    global imagen3
    imagen3 = Image.open(archivo)
    imagen3resiz = imagen3.resize((200,200), Image.Resampling.LANCZOS)
    render3 = ImageTk.PhotoImage(imagen3resiz)    
    lbl3.configure(image=render3)
    lbl3.image = render3


def filtro():
    imagen4 = Image.open(r"C:\Users\WilliamMon\Documents\Practicas_Program3_UGB\Semana11\imagen5.jpg")
    filtro = imagen4.filter(ImageFilter.DETAIL)
    imagen4resiz = filtro.resize((200,200), Image.Resampling.LANCZOS)
    render4 = ImageTk.PhotoImage(imagen4resiz)    
    lbl4.configure(image=render4)
    lbl4.image = render4

def convertir():
    img5 = imagen3
    imgbn = img5.convert("L")
    imgbnresiz = imgbn.resize((200,200), Image.Resampling.LANCZOS)
    render5 = ImageTk.PhotoImage(imgbnresiz)    
    lbl3.configure(image=render5)
    lbl3.image = render5



class Funciones():

    def mostrar(self):
        imagen1 = Image.open(r"C:\Users\WilliamMon\Documents\Practicas_Program3_UGB\Semana11\lenguaje.jpg")
        imagen1resiz = imagen1.resize((200,200), Image.Resampling.LANCZOS)
        render1 = ImageTk.PhotoImage(imagen1resiz)    
        lbl1.configure(image=render1)
        lbl1.image = render1


    def cargar(self):
        archivo = filedialog.askopenfilename()
        self.imagen3 = Image.open(archivo)
        imagen3resiz = self.imagen3.resize((200,200), Image.Resampling.LANCZOS)
        render3 = ImageTk.PhotoImage(imagen3resiz)    
        lbl3.configure(image=render3)
        lbl3.image = render3


    def filtro(self):
        imagen4 = Image.open(r"C:\Users\WilliamMon\Documents\Practicas_Program3_UGB\Semana11\imagen5.jpg")
        filtro = imagen4.filter(ImageFilter.DETAIL)
        imagen4resiz = filtro.resize((200,200), Image.Resampling.LANCZOS)
        render4 = ImageTk.PhotoImage(imagen4resiz)    
        lbl4.configure(image=render4)
        lbl4.image = render4

    def convertir(self):
        img5 = self.imagen3
        imgbn = img5.convert("1")
        imgbnresiz = imgbn.resize((200,200), Image.Resampling.LANCZOS)
        render5 = ImageTk.PhotoImage(imgbnresiz)    
        lbl3.configure(image=render5)
        lbl3.image = render5



ventana = Tk()
ventana.geometry("400x400")

imagen2 = Image.open(r"C:\Users\WilliamMon\Documents\Practicas_Program3_UGB\Semana11\Conferencia.jpeg")
imagen2resiz = imagen2.resize((200,200), Image.Resampling.LANCZOS)
render2 = ImageTk.PhotoImage(imagen2resiz)
funcion = Funciones()
btn1 = Button(ventana, text="Mostrar Imagen", command=funcion.mostrar)
btn2 = Button(ventana, text="Cargar Imagen", command=funcion.cargar)
btn3 = Button(ventana, text="Aplicar filtro Imagen", command=funcion.filtro)
btn4 = Button(ventana, text="Convertir a B/N", command=funcion.convertir)
lbl1 = Label(ventana, image="")
lbl2 = Label(ventana, image=render2)
lbl3 = Label(ventana, image="")
lbl4 = Label(ventana, image="")

lbl1.pack()
lbl2.pack()
lbl3.pack()
lbl4.pack()
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()

ventana.mainloop()




