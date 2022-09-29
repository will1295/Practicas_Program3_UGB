from PIL import Image, ImageTk, ImageFilter
from tkinter import Tk, Label, Button, filedialog

def cargar():
    archivo = filedialog.askopenfilename()
    global imagen
    imagen = Image.open(archivo)
    imagenres = imagen.resize((200,200), Image.Resampling.LANCZOS)
    render = ImageTk.PhotoImage(imagenres)
    label1.configure(image=render)
    label1.image = render

#def filtro():
#    archivo2 = filedialog.askopenfilename()
#    imagen2 = Image.open(archivo2)
#    imgfiltro = imagen2.filter(ImageFilter.CONTOUR)
    #imgfiltro.save("Imagen_con_Filtro.jpg")
    #imgfiltro.show()
#    imagenres2 = imgfiltro.resize((200,200), Image.Resampling.LANCZOS)
#    render2 = ImageTk.PhotoImage(imagenres2)
#    label2.configure(image=render2)
#    label2.image = render2
    
def filtro():
    imagenfiltro = imagen
    imgfiltro = imagenfiltro.filter(ImageFilter.CONTOUR)
    imagenres3 = imgfiltro.resize((200,200), Image.Resampling.LANCZOS)
    render3 = ImageTk.PhotoImage(imagenres3)
    label1.configure(image=render3)
    label1.image = render3
    

class Metodos:

    def __init__(self):
        self.imagen= ""


    def cargar(self):
        archivo = filedialog.askopenfilename()
        self.imagen = Image.open(archivo)
        imagenres = self.imagen.resize((200,200), Image.Resampling.LANCZOS)
        render = ImageTk.PhotoImage(imagenres)
        label1.configure(image=render)
        label1.image = render
        
    def filtro(self):
        imagenfiltro = self.imagen
        imgfiltro = imagenfiltro.filter(ImageFilter.CONTOUR)
        imagenres3 = imgfiltro.resize((200,200), Image.Resampling.LANCZOS)
        render3 = ImageTk.PhotoImage(imagenres3)
        label1.configure(image=render3)
        label1.image = render3


ventana = Tk()
ventana.geometry("300x300")
metodo = Metodos()
label1 = Label(ventana, image="")
label2 = Label(ventana, image="")
boton1 = Button(ventana, text="Cargar imagen", command=metodo.cargar)
boton2 = Button(ventana, text= "Aplicar filtro", command=metodo.filtro)

label1.pack()
label2.pack()
boton1.pack()
boton2.pack()

ventana.mainloop()




