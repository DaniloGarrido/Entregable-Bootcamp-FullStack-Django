from django.shortcuts import render, redirect
from urllib import request

from core.models import Cliente,Contacto
from .forms import formCli,formCon
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
            
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'El usuario o la contraseña es incorrecta')

    context = {}
    return render (request,'registration/login.html',context)

def index(request):
    return render(request,'index.html')

def feriados(request):
    return render (request,'apiferiados.html')
#CRUD Cliente
def mostrarCli(request):
    clientes = Cliente.objects.all()      #similar al comando select
    datos = {
        'clientes' : clientes
    }
    return render (request, 'mostrarCli.html', datos)

def crearCliente(request):
    if request.method=='POST':
        forms_cliente=formCli(request.POST)
        if forms_cliente.is_valid():
            forms_cliente.save()
            return redirect('mostrarCli')
    else:
        forms_cliente=formCli()
    return render(request,'ingresar_cli.html',{'form_cliente':forms_cliente})

def modiCli(request, id):
    cliente = Cliente.objects.get(idCli = id) #similar al select where
    datos ={
        'form': formCli(instance=cliente)
    }
    if request.method == 'POST':
        formulario = formCli(data = request.POST, instance = cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect ('mostrarCli')
    return render (request, 'modiCli.html',datos)

def delCli(request, id): 
    cliente = Cliente.objects.get(idCli = id)
    cliente.delete()
    return redirect ('mostrarCli')
    
#Fin CRUD Cliente
#CRUD Contacto
def crearContacto(request):
    if request.method=='POST':
        forms_contacto=formCon(request.POST)
        if forms_contacto.is_valid():
            forms_contacto.save()
            return redirect('mostrarCli')
    else:
        forms_contacto=formCon()
    return render(request,'contactanos.html',{'form_contacto':forms_contacto})
