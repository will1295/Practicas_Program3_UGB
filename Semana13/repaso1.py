from tkinter import Tk, Button, Label, Entry, Text

def On_Click():
    #button1.config(text="Texto cambiado")
    button1["text"]="Texto 2"
    button1.config(bg="red")


ventana = Tk()
ventana.geometry("400x400")


label1=Label(ventana, text="Esto es un label")
button1=Button(ventana, text="Esto es un boton", command=On_Click)
entry1= Entry(ventana)
text1=Text(ventana)
#label1.pack()
#button1.pack()
#entry1.pack()
#text1.pack()


#label1.place(relx=0.2,rely=0.4, relwidth=0.3, relheight=0.3)
label1.grid(row=0,column=0,columnspan=2,  padx=10, pady=1)
button1.grid(row=0,column=3, padx=1, pady=1)


ventana.mainloop()

