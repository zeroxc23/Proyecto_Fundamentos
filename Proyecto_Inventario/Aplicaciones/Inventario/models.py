from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_lenght= 100)
    descripcion =  models.TextField(blank= True, null= True)

    def __str__(self):
        return self.nombre

class inventario(models.model):
    codigo = models.CharField(primary_key=True, max_length= 8)
    descripcion = models.CharField(max_length= 100)
    categoria =
