from django.shortcuts import render
from django.template import context
from django.http import HttpResponse
from .models import Clientes

# Create your views here.



def index(request):
    return render(request,'index.html',{"username":"Carlitos",
    "username2":"Maria"})


def about(request):
    return render(request,'about.html') 

def prueba(request):
    return render(request,'prueba.html')     

def formulario(request):
    return render(request,'formulario.html')

def adminclientes(request):
    listacli = Clientes.objects.all()
    return render(request,'clientescrud.html', {"cliente":listacli})    