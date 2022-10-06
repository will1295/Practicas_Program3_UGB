from os import environ
from source import email
from dotenv import load_dotenv

load_dotenv()


mensaje_html="""

<!DOCYPE html>
<html>
<body>
<h1>Saludos desde python {}</h1>
<p>{}</p>
</body>
</html>

"""
origen=input("Desde donde se manda los correos: ")
environ["STMP_USER"]=origen
nombre=input("A quién quieres mandarle tu correo? ")
destinatario=input("Escribe el correo de la persona: ")
mensaje=""
Correo = email.Email()
Correo.mandar_email([destinatario],"Prueba Python", message_format=mensaje_html.format(nombre,mensaje), format="html")
