#Importancion de tkinter
from tkinter import Tk, Entry, Label, Button, Radiobutton, IntVar, messagebox
#Importacion de ttk
from tkinter.ttk import Combobox

def imprimir():
    #Obtener informacion de los widgets
    #Obteniendo el valor de los raddiobutton
    valor=str(radio.get())
    #Obteniendo el valor del input
    txt=str(input1.get())
    #Obteniendo el valor del combobox
    lista = str(combo.get())
    messagebox.showinfo(title="Valor del radio", message=valor+" "+txt+" "+lista)


vent1= Tk()
vent1.geometry("200x200")

radio = IntVar()

labl1=Label(vent1, text="Label 1")
input1=Entry(vent1)
labl2=Label(vent1, text="Label 2")
input2=Entry(vent1)
#Declaracion de los radio button
rdb1 = Radiobutton(vent1, text="Opcion 1", value=1, variable=radio)
rdb2 = Radiobutton(vent1, text="Opcion 2", value=2, variable=radio)

btn1 = Button(vent1,text="Boton",command=imprimir)
#Declaracion de combobox y valores
combo = Combobox(vent1,state="readonly")
combo['values']=("Opcion 1","Opcion2")

#Mapeo de widgets
labl1.pack()
input1.pack()
labl2.pack()
input2.pack()
btn1.pack()
rdb1.pack()
rdb2.pack()
combo.pack()

vent1.mainloop()