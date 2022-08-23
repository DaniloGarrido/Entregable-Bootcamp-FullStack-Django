from turtle import textinput
from django import forms
from django.forms import ModelForm, NumberInput
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import  Cliente, Contacto


class formCli(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['idCli', 'nomCli', 'apeCli', 'correoCli','fonoCli','direccionCli']
        labels ={
            'idCli': 'ID', 
            'nomCli': 'Nombre', 
            'apeCli': 'Apellido', 
            'correoCli': 'Correo', 
            'fonoCli': 'Fono',
            'direccionCli': 'Direccion',
        }
        widgets={
            'idCli': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingresa un id', 
                    'id': 'idCli'
                }
            ), 
            'nomCli': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre', 
                    'id': 'nomCli'
                }
            ), 
            'apeCli': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Apellido', 
                    'id': 'apeCli'
                }
            ), 
            'correoCli': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese Email',
                    'id': 'correoCli'
                }
            ),
             'fonoCli': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese Fono',
                    'id': 'fonoCli',
                }
            ),
            'direccionCli': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese direccion',
                    'id': 'direccionCli',
                }
            )
        }
class formCon(forms.ModelForm):

    class Meta: 
        model= Contacto
        fields = ['idCon', 'nomCon', 'apeCon', 'correoCon','fonoCon','motiCon','comentCon']
        labels ={
            'idCon': 'ID', 
            'nomCon': 'Nombre', 
            'apeCon': 'Apellido', 
            'correoCon': 'Correo', 
            'fonoCon': 'Fono',
            'direccionCon': 'Direccion',
        }
        widgets={
            'idCon': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingresa un id', 
                    'id': 'idCon'
                }
            ), 
            'nomCon': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese un Nombre', 
                    'id': 'nomCon'
                }
            ), 
            'apeCon': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese un Apellido', 
                    'id': 'apeCon'
                }
            ), 
            'correoCon': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese un Email',
                    'id': 'correoCon'
                }
            ),
             'fonoCon': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese un Telefono',
                    'id': 'fonoCon',
                }
            ),
            'motiCon': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Seleccione un motivo de la consulta',
                    'id': 'motiCon',
                }
            ),
            'comentCon': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese sus comentarios',
                    'id': 'comentCon',
                }
            )
        }
 