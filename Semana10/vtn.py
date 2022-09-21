import tkinter as tk
from tkinter import messagebox
#from tkinter import*

#Funcion que muestra hola mundo
def ejemplo():
    print("Hola mundo")
    messagebox.showinfo(title="Hola mundo")
    
#Funcion que retorna un mensaje escrito en el input
def mensaje():
    variable=caja.get()
    messagebox.showinfo(title="Prueba",message=variable)

ventana= tk.Tk()
ventana.geometry("400x400")
#btn1= tk.Button(ventana, text= "Boton",bg="Red",command=ejemplo)
btn1= tk.Button(ventana, text= "Boton",bg="Red",command=ejemplo)
caja = tk.Entry(ventana)
texto = tk.Label(ventana,text="Esto es un label")
caja2 = tk.Entry(ventana)
texto2 = tk.Label(ventana,text="Esto es un label 2")
op = tk.Radiobutton(ventana, text="Opcion 1", value=1)
op2 = tk.Radiobutton(ventana, text="Opcion 2", value=2)

#Metodo de localizacion grid
caja.grid(row=0,column=0)
texto.grid(row=0,column=1)
btn1.grid(row=0,column=2)

caja2.grid(row=1,column=0)
texto2.grid(row=1,column=1)


#Posicion relativa
#caja.place(relx=0.02,rely=0.02, relwidth=0.5)


"""
#Posicion absoluta
caja.place(x=50,y=10, width=100)
texto.place(x=170,y=10, width=100)
caja2.place(x=50,y=50, width=100)
texto2.place(x=170,y=50, width=100)
btn1.place(x=170, y=80, height = 30, width=100)
op.place(x=50, y=150, height = 50, width=100)
op2.place(x=150, y=150, height = 50, width=100)

#Metodo pack de localizacion
caja.pack()
btn1.pack(side='left')
texto.pack(side='bottom')
op.pack(side='right')
op2.pack(side='top')
"""
ventana.mainloop()