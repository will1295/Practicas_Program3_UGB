import PIL
from PIL import Image, ImageTk
from tkinter import Tk,Button, Label, filedialog

#def mostrar():
#    imagen1= Image.open(r"C:\Users\WilliamMon\Documents\Practicas_Program3_UGB\Semana11\Conferencia.jpeg")
#    imagen1.show()

def cargar():
    archivo = filedialog.askopenfilename()
    foto2 = Image.open(archivo)
    render2 = ImageTk.PhotoImage(foto2)
    label2.configure(image=render2)
    label2.image = render2

def convertir():
    bn = imagen2.convert("L")
    bn.save("blancn.jpg")
    bn.show()


ventana = Tk()
ventana.geometry("500x500")
imagen2 = Image.open(r"C:\Users\WilliamMon\Documents\Practicas_Program3_UGB\Semana11\Conferencia.jpeg")
reducida = imagen2.resize((300,300), Image.Resampling.LANCZOS)
render =ImageTk.PhotoImage(reducida)

label1 = Label(ventana, image=render)
label2 = Label(ventana, image="")
boton2 = Button(ventana, text="Cargar foto", command=cargar)
boton3 = Button(ventana, text="Convertir a B/N", command=convertir)
#boton1= Button(ventana,text="Mostrar foto", command=mostrar) 
#boton1.pack()
label1.pack()
label2.pack()
boton2.pack()
boton3.pack()

ventana.mainloop()



