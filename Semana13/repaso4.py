from tkinter import END, Tk, Button, Label, Entry, ttk, messagebox
from fractions import Fraction

def calcular():
    d1=denom1.get()
    n1=num1.get()
    d2=denom2.get()
    n2=num2.get()
    op=combo1.get()
    num3.delete(0,END)
    denom3.delete(0,END)

    if(d1=="" or n1=="" or d2=="" or n2==""):
        messagebox.showerror(title="Error", message="Debe rellenar todos los campos")
    else:   
        #Mismo denominador            
        if(op=="sumar"):
            resulnum=float(n1)+float(n2)
            resuldenom=d1
            num3.insert(0,resulnum)
            denom3.insert(0,resuldenom)
        #Mismo denominador
        elif(op=="restar"):
            resulnum=float(n1)-float(n2)
            resuldenom=d1
            num3.insert(0,resulnum)
            denom3.insert(0,resuldenom)
        elif(op=="multiplicar"):
            resulnum=float(n1)*float(n2)
            resuldenom=float(d1)*float(d2)
            num3.insert(0,resulnum)
            denom3.insert(0,resuldenom)
        elif(op=="dividir"):
            resulnum=float(n1)*float(d2)
            resuldenom=float(d1)*float(n2)
            num3.insert(0,resulnum)
            denom3.insert(0,resuldenom)
        else:
            messagebox.showerror(title="Error", message="Operacion invalida")
   




ventana = Tk()
ventana.geometry("400x400")

label1= Label(ventana,text="Fraccion 1")
num1=Entry(width=5)
denom1=Entry(width=5)
label2 = Label(ventana,text="Fraccion 2")
num2=Entry(width=5)
denom2=Entry(width=5)
label3 = Label(ventana,text="Resultado")
num3=Entry(width=5)
denom3=Entry(width=5)
combo1=ttk.Combobox(ventana, 
                        values=["sumar","restar","multiplicar","dividir"],state="readonly")
boton1= Button(ventana, text="Calcular", command=calcular)


label1.grid(row=0,column=0)
num1.grid(row=0,column=1)
denom1.grid(row=1,column=1)
label2.grid(row=0,column=2)
num2.grid(row=0,column=3)
denom2.grid(row=1,column=3)
label3.grid(row=2,column=2)
num3.grid(row=2,column=3)
denom3.grid(row=3,column=3)
combo1.grid(row=4,column=2)
boton1.grid(row=5,column=2)



ventana.mainloop()