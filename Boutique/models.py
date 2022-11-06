from django.db import models

# Create your models here.

class tblusuario(models.Model):
    usuario = models.CharField(max_length = 15)
    password = models.CharField(max_length = 10)
    permiso = models.TextField(max_length = 50)

class tblproducto(models.Model):
    nombre = models.CharField(max_length = 100)
    tipo = models.CharField(max_length = 100)
    Marca = models.CharField(max_length = 100)
    descriocion = models.TextField(max_length = 100)
    stock = models.IntegerField()
    precio = models.IntegerField()

'''
class tblcompra(models.Model):
    cliente = models.ForeignKey(tblusuario, on_delete = models.CASCADE)
    nombre_pdto= models.ForeignKey(tblproducto, on_delete = models.CASCADE)
    valor = models.ForeignKey(tblproducto, on_delete = models.CASCADE)
    total =models.IntegerField()
'''