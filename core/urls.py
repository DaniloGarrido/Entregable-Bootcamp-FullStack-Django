from unicodedata import name
from django.urls import path 
from .views import crearCliente, index,login,feriados,mostrarCli,modiCli,delCli,crearContacto
urlpatterns=[ 
    path('index/', index, name="index"),
    path('login/',login,name="login"),
    #URL CRUD Cliente
    path('crearCliente/',crearCliente,name="crearCliente"),
    path('mostrarCli/',mostrarCli,name="mostrarCli"),
    path('modiCli/<id>',modiCli,name="modiCli"),
    path('delCli/<id>',delCli,name="delCli"),
    #Fin
    #URL CRUD Contacto
    path('crearContacto/',crearContacto,name="crearContacto"),


    path("feriados/", feriados, name="feriados"),
   

    #path('registro/', registro, name="registro"),
    
    #path('crearVehiculoForm/',crearVehiculoForm,name="crearVehiculoForm"),
    #path('form_modVehiculo/<id>',form_modVehiculo,name="form_modVehiculo"),
    #path('form_elimVehiculo/<id>',form_elimVehiculo,name="form_elimVehiculo"),
]