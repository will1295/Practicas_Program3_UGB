#import tkinter as tk
from tkinter import Tk, Entry, Label, Button, Radiobutton, IntVar
from tkinter.ttk import Combobox

interfaz = Tk()
interfaz.geometry("200x200")
radio= IntVar()

txt1 = Label(interfaz, text="Esto es un label")
cajatxt1 = Entry(interfaz)
txt2 = Label(interfaz, text="Esto es otro label")
cajatxt2 = Entry(interfaz)
btn = Button(interfaz, text="Esto es un boton")
rdb1 = Radiobutton(interfaz, text="Opcion 1", value=1, variable=radio)
rdb2 = Radiobutton(interfaz, text="Opcion 2", value=2, variable=radio)
combo = Combobox(interfaz)
txt1.pack()
cajatxt1.pack()
txt2.pack()
cajatxt2.pack()
btn.pack()
rdb1.pack()
rdb2.pack()
combo.pack()

interfaz.mainloop()


