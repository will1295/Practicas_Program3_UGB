from django.urls import path
from .views import index, acercade, base, registro, clientes, regclientes

urlpatterns = [
    path('', index, name="inicio"),
    path('about/', acercade, name="about"),
    path('base/',base),
    path('login/',registro),
    path('clientes/',clientes),
    path('regclientes/',regclientes)
]
