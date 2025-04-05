from django.db import models
from django.forms import ValidationError

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre 
    
class Proveedor (models.Model):
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True) 

    def __str__(self):
        return self.nombre
    
class Producto (models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def clean(self):
        if self.stock < 0:
            raise ValidationError("El stock no puede ser negativo.")

    def __str__(self):
        return f"{self.nombre} - {self.stock} en stock"