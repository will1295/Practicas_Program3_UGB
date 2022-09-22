#import xhtml2pdf
from xhtml2pdf import pisa
import os

direccion = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
archivo_html =open(os.path.join(direccion,'Semana10\pagina.html')).read()

#archivo_html= "<html><body><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit</p><body/></html>"
archivo_pdf="convertido2.pdf"

def convertir_html_a_pdf(archivo_html,archivo_pdf):
    archivo= open(archivo_pdf, "w+b")

    estado= pisa.CreatePDF(archivo_html, dest=archivo)
    archivo.close()
    return estado.err

if __name__ == "__main__":
    pisa.showLogging()
    convertir_html_a_pdf(archivo_html, archivo_pdf)