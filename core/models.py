from django.db import models

# Create your models here.
class Cliente (models.Model):
    idCli=models.AutoField(primary_key=True, verbose_name="Id cliente")
    nomCli=models.CharField(max_length=50,verbose_name="Nombre")
    apeCli=models.CharField(max_length=50,verbose_name="Apellido")
    correoCli=models.EmailField(max_length=60,verbose_name="Correo electronico")
    fonoCli=models.IntegerField(verbose_name="Telefono")
    direccionCli=models.CharField(max_length=100,verbose_name="Direccion")
    
    def __str__(self):
        return self.idCli
class Contacto(models.Model):
    idCon=models.AutoField(primary_key=True, verbose_name="Id del contacto")
    nomCon=models.CharField(max_length=50,verbose_name="Nombre")
    apeCon=models.CharField(max_length=50,verbose_name="Apellido")
    correoCon=models.EmailField(max_length=60,verbose_name="Correo electronico")
    fonoCon=models.IntegerField(verbose_name="Telefono")
    opciones=(
        ('c','consulta'),
        ('r','reclamo')
    )
    motiCon=models.CharField(max_length=1,choices=opciones,default='c')
    comentCon=models.TextField(max_length=200,verbose_name="Comentarios")
    def __str__(self):
        return self.idCon