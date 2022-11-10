from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="principal"),
    path('about/', about, name="acercade"),
    path('prueba', prueba),
    path('formulario/', formulario, name="form")
]