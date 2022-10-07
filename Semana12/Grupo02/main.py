from dotenv import load_dotenv
from os import environ
from source import email

load_dotenv()

mensaje="""
<!DOCTYPE html> 
<html> 
<head> 
<title></title>
</head> 
<body> 
<h1 align="center" >Saludos {} desde Python</h1> 
<hr>
<p>Esto es un mensaje realizado de manera automática.</p> 
<img> 
</body> 
</html> 
"""

origen=input("Digita tu correo: ")
nombre=input("A quien quieres mandarle un correo? ")
correo=input("Digita el corro de esa persona ")


environ["SMPT_USER"]=origen




Correo = email.Email()
imagen=Correo.imagen
Correo.mandar_correo([correo],"Prueba2",message_format=mensaje.format(nombre),format="html")