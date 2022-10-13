from tkinter import END, Tk, Button, Label, Entry, Text
from fractions import Fraction
from tkinter import ttk

def On_Click():
  
    num3.delete(0,END)
    denom3.delete(0,END)
    n1= float(num1.get()) 
    d1= float(denom1.get())
    n2 = float(num2.get())
    d2 = float(denom2.get())


    op = combo1.get()
    if(op=="Suma"):
        suma=Fraction(n1/d1)+Fraction(n2/d2)
        num3.insert(0,suma.numerator)
        denom3.insert(0,suma.denominator)

    elif(op=="Resta"):
        suma=Fraction(n1/d1)-Fraction(n2/d2)
        num3.insert(0,suma.numerator)
        denom3.insert(0,suma.denominator)
    elif(op=="Multiplicacion"):
        resulnum=n1*n2
        resuldem=d1*d2
        num3.insert(0,resulnum)
        denom3.insert(0,resuldem)
    elif(op=="Division"):
        resulnum=n1*d2
        resuldem=d1*n2
        num3.insert(0,resulnum)
        denom3.insert(0,resuldem)
    else:
        print("Operacion invalida")



ventana1 = Tk()
ventana1.geometry("300x400")

label1=Label(ventana1, text="Primera fraccion")
num1= Entry(ventana1, width=5)
denom1= Entry(ventana1, width=5)
label2=Label(ventana1, text="Segunda fraccion")
num2= Entry(ventana1, width=5)
denom2= Entry(ventana1, width=5)


label3=Label(ventana1, text="Resultado")
num3= Entry(ventana1, width=5)
denom3= Entry(ventana1, width=5)

label4=Label(ventana1, text="Operaciones")
#valores = ["Suma", "Resta", "Multiplicacion", "Division"]
combo1 = ttk.Combobox(ventana1, state="readonly", 
                      values=["Suma", "Resta", "Multiplicacion", "Division"])

button1=Button(ventana1, text="Calcular", command=On_Click)


label1.grid(row=0,column=0)
num1.grid(row=0,column=1)
denom1.grid(row=1,column=1)
label2.grid(row=0,column=2)
num2.grid(row=0,column=3)
denom2.grid(row=1,column=3)
"""

label3.pack()
num3.pack()
denom3.pack()
label4.pack()
combo1.pack()
button1.pack()
"""

ventana1.mainloop()