#import PIL 
from PIL import Image, ImageTk
from tkinter import Tk, Button, Label, filedialog

def mostrar():
    imagen1 = Image.open(r"C:\Users\WilliamMon\Documents\Practicas_Program3_UGB\Semana11\Conferencia.jpeg")
    imagen1.show()

def convertir():  
    imagen3 = Image.open(r"C:\Users\WilliamMon\Documents\Practicas_Program3_UGB\Semana11\lenguaje.jpg")
    imagen3bn = imagen3.convert("L")
    imagen3bn.save("blanco_negro.jpg")
    imagen3bn.show()  

def cargar():
    archivo = filedialog.askopenfilename()
    imagen4 = Image.open(archivo)
    imagenresiz2 = imagen4.resize((100,100),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    label2.configure(image=render2)
    label2.image = render2

ventana = Tk()
ventana.geometry("300x300")

imagen2 = Image.open(r"C:\Users\WilliamMon\Documents\Practicas_Program3_UGB\Semana11\minerva.jpg")
imagenresiz = imagen2.resize((100,100),Image.Resampling.LANCZOS)
render = ImageTk.PhotoImage(imagenresiz)


label1 = Label(ventana, image=render)
label2 = Label(ventana, image="")
btn1=Button(ventana, text="Mostrar imagen", command=mostrar)
btn2=Button(ventana, text="Guardar en B/N", command=convertir)
btn3=Button(ventana, text="Cargar", command=cargar)
btn1.pack()
btn2.pack()
btn3.pack()
label1.pack()
label2.pack()
ventana.mainloop()



