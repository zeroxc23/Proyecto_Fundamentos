from django.db import models

# Modelos Para la Base de Datos

# Categorias

class Categoria(models.Model):
    id = models.BigAutoField(primary_key= True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length= 200)
    def __str__(self):
        return self.nombre
    
# Proovedores

class Proveedor(models.Model):
    id = models.BigAutoField(primary_key= True)
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(max_length=20)
    correo = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

    

# Productos

class Producto(models.Model):
    id = models.BigAutoField(primary_key= True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length= 200)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, default=None)
    proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE, default=None)
    cantidad = models.PositiveBigIntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.nombre, self.descripcion)

