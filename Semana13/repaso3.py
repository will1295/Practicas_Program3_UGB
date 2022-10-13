from cgitb import text
from tkinter import Tk, Label, Button, Entry, Text





ventana1= Tk()
ventana1.geometry("400x400")

def On_click():
    #label1["text"]="Texto cambiado"
    label1.config(text="Texto cambiado 2", bg="red")

    #text1.insert(0,"Texto")

label1=Label(ventana1, text="Esto es un label")
boton1=Button(ventana1, text="Esto es un boton", command=On_click)
entry1 = Entry(ventana1)
text1 = Text(ventana1)

label1.grid(row=0,column=0)
boton1.grid(row=0,column=1)
boton1.grid(row=1,column=0)
entry1.grid(row=1,column=1)
#text1.grid(row=2,column=0)


ventana1.mainloop()