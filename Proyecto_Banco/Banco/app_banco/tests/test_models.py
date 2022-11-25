from django.test import TestCase
from app_banco.models import *

class TestModels(TestCase):

    def test_model(self):
        self.Clienteprueba = Clientes.objects.create(
            codigo=123456,
            nombre="juan",
            apellido="perez",
            telefono=123456789,
            direccion="prueba"
        )

    