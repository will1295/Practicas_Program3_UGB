from django.test import TestCase
from Pharmacy_app.models import *

class TestModels(TestCase):

    def test_model(self):
        self.Clienteprueba = Clientes.objects.create(
            codigo=123456,
            nombre="juan",
            apellido="perez",
            telefono=123456789,
            direccion="prueba"
        )

    