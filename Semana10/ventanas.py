#import tkinter as tk
from tkinter import Tk, Entry, Label, Button, Radiobutton, IntVar, messagebox
from tkinter.ttk import Combobox


def funcion():
    messagebox.showinfo(title="Prueba", message="Hola mundo")

def valores():
    texto1=cajatxt1.get()
    texto2=cajatxt2.get()
    rad=str(radio.get())
    cmb=combo.get()
    frase=f"El valor del primer input es: {texto1}, el del segundo es: {texto2}, el valor del radiobutton escogido es: {rad} y el valor del combobox es: {cmb}"
    messagebox.showinfo(title="Valores", message=frase)



interfaz = Tk()
interfaz.geometry("200x200")
radio= IntVar()
txt1 = Label(interfaz, text="Esto es un label")
cajatxt1 = Entry(interfaz)
txt2 = Label(interfaz, text="Esto es otro label")
cajatxt2 = Entry(interfaz)
btn1 = Button(interfaz, text="Valores", command=valores)
btn2 = Button(interfaz, text="Esto es un boton", command=funcion)
rdb1 = Radiobutton(interfaz, text="Opcion 1", value=1, variable=radio)
rdb2 = Radiobutton(interfaz, text="Opcion 2", value=2, variable=radio)
combo = Combobox(interfaz, state="readonly")
combo['values']=("valor1","valor2","valor3")

"""
Posiciones absolutas
txt1.place(x=50,y=20,width=100, height=50)
cajatxt1.place(x=50,y=80,width=100, height=20)
"""

"""
txt1.place(relx=0.2,rely=0.2,relwidth=0.5, relheight=0.1)
cajatxt1.place(relx=0.2,rely=0.4,relwidth=0.5, relheight=0.1)
"""

"""
txt1.grid(row=0,column=0, columnspan=2,rowspan=2)
txt2.grid(row=0,column=3,rowspan=2)
cajatxt1.grid(row=3,column=0, columnspan=2, padx=20,pady=10)
cajatxt2.grid(row=3,column=3,padx=20,pady=10)
"""
txt1.pack()
cajatxt1.pack()
txt2.pack()
cajatxt2.pack()
rdb1.pack()
rdb2.pack()
combo.pack()
btn1.pack()
btn2.pack()


"""
txt1.pack(ipadx=20)
cajatxt1.pack(ipady=20)
txt2.pack(side="top")
cajatxt2.pack(side="bottom")
btn.pack(fill="both")
rdb1.pack()
rdb2.pack()
combo.pack(expand=10)
"""

interfaz.mainloop()


