from django.urls import path
from .views import index, acercade, base

urlpatterns = [
    path('', index, name="inicio"),
    path('about/', acercade, name="about"),
    path('base/',base)
]
