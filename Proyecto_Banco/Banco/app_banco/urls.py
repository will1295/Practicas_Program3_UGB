from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="inicio"),
    path('about/', acercade, name="about"),
    path('base/',base),
    path('registro/',registro, name="registro"),
    path('adminclientes/',adminclientes, name="adminclientes"),
    path('agregarcliente/',agregarcliente),
    path('delclientes/<id>',delclientes, name="delcientes"),
    path('editclientes/<id>',editclientes, name="editcientes"),
    path('actualizarcliente/<id>',actualizarclientes,name="actualizarclientes"),
]


