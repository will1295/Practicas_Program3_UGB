from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name="principal"),
    path('about/', about, name="acercade"),
    path('prueba', prueba),
    path('registro/', registro,name="registro"),
    path('', vistalogin,name="login"),
    path('logout/', cerrarsesion,name="cerrarsesion"),
    path('formulario/', formulario, name="form"),
    path('clientes/', adminclientes, name="adminclientes"),
    path('addclientes/', addclientes, name="admincliente"),
    path('delcliente/<id>', delcliente, name="delcliente"),
    path('editcliente/<id>', editcliente, name="editcliente"),
    path('guardarcliente/<id>', guardarcliente, name="guardarcliente"),

]