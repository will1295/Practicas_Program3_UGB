from os import getenv
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from typing import List, Optional

class Email:
    def __init__(self):
        self.Server = SMTP(
            host=getenv("SMTP_HOSTNAME"),
            port=getenv("SMTP_PORT")
        )
        self.imagen=open(r'C:\Users\WilliamMon\Documents\Practicas_Program3_UGB\Semana12\Practica12\source\alan.jpg','rb').read()
        self.imagenmime=MIMEImage(self.imagen,'jpg')

    def conectar(self):
        self.Server.starttls()
        self.Server.login(
            user=getenv("SMPT_USER"),
            password=getenv("SMTP_PASSWORD")
        )

    def mandar_correo(self,correo:List[str],asunto:Optional[str], **kwargs):
        self.conectar()
        for em in correo:
            mime= MIMEMultipart()
            mime['From']=getenv("SMPT_USER")
            mime['To']=em
            mime['Subject']=asunto
            format=MIMEText(kwargs['message_format'],kwargs['format'])
            mime.attach(format)
            imagen=open(r'C:\Users\WilliamMon\Documents\Practicas_Program3_UGB\Semana12\Practica12\source\alan.jpg','rb').read()
            imagenmime=MIMEImage(imagen,'jpg')
            mime.attach(imagenmime)
            self.Server.sendmail(getenv("SMPT_USER"),em,mime.as_string())
            self.desconectar()



    def desconectar(self):
        self.Server.quit()
        self.Server.close()