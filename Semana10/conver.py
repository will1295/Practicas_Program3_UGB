from xhtml2pdf import pisa
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
source_html= open(os.path.join(base_dir,'Practicas_Program3_UGB/prueba2.html')).read()
#source_html= "<html><body><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum</p></body></html>"
output_filename = "prueba2.pdf"

def convert(source_html,output_filename):
    result_file= open(output_filename, "w+b")

    pisa_status = pisa.CreatePDF(source_html, dest=result_file)
    result_file.close()
    return pisa_status.err

#Programa principal

if __name__ == "__main__":
    pisa.showLogging()
    convert(source_html, output_filename)
