from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Proveedor, Producto
from django.contrib import messages




#/////////////////////////////////////////////////////////////////////////////////////
# Sección Inventario

# Página de Inventario
def homeinvent(request):
    productos_listados = Producto.objects.all()
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()
    messages.success(request, '¡Productos listados!')
    return render(request, "gestionInventario.html", {
        "productos": productos_listados,
        "categorias": categorias,
        "proveedores": proveedores
    })

# Registrar Producto
def registrarProducto(request):
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        descripcion = request.POST['txtDescripcion']
        categoria_id = request.POST['txtCategoria']
        proveedor_id = request.POST['txtProveedor']
        precio = request.POST['txtPrecio']
        cantidad = request.POST['txtCantidad']

        categoria = get_object_or_404(Categoria, id=categoria_id)
        proveedor = get_object_or_404(Proveedor, id=proveedor_id)

        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            categoria=categoria,
            proveedor=proveedor,
            precio=precio,
            cantidad=cantidad
        )

        messages.success(request, '¡Producto registrado!')
    return redirect('IndexInvent')

# Formulario de edición
def edicionProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.precio = str(producto.precio)
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()
    return render(request, "editarInventario.html", {
        "producto": producto,
        "categorias": categorias,
        "proveedores": proveedores
    })

# Guardar edición
def editarProducto(request):
    if request.method == 'POST':
        id = request.POST['txtId']
        nombre = request.POST['txtNombre']
        descripcion = request.POST['txtDescripcion']
        categoria_id = request.POST['txtCategoria']
        proveedor_id = request.POST['txtProveedor']
        precio = request.POST['txtPrecio']
        cantidad = request.POST['txtCantidad']

        producto = get_object_or_404(Producto, id=id)
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.categoria = get_object_or_404(Categoria, id=categoria_id)
        producto.proveedor = get_object_or_404(Proveedor, id=proveedor_id)
        producto.precio = precio
        producto.cantidad = cantidad
        producto.save()

        messages.success(request, '¡Producto actualizado!')
    return redirect('IndexInvent')

# Eliminar producto
def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, '¡Producto eliminado!')
    return redirect('IndexInvent')


#/////////////////////////////////////////////////////////////////////////////////////

#Sección Categoria
def homecategoria(request):
    categorias=Categoria.objects.all()
    messages.success(request,'¡Categoria listada!')
    return render(request,"gestionCategoria.html",{
        "categorias":categorias,
    })

# Registrar Categoria
def registrarCategoria(request):
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        descripcion = request.POST['txtDescripcion']

        Categoria.objects.create(
            nombre=nombre,
            descripcion=descripcion
        )

        messages.success(request, '¡Categoría registrada!')

    
    return redirect('IndexCat')


# Formulario de edición
def edicionCategoria(request,id):
    categorias = get_object_or_404(Categoria, id=id)
    return render(request,"editarCategoria.html",{
        "categorias":categorias,
    })

#Guardar edición
def editarCategoria(request):
    if request.method == 'POST':
        id = request.POST['txtId']
        nombre = request.POST['txtNombre']
        descripcion = request.POST['txtDescripcion']

        categoria = get_object_or_404(Categoria, id=id)
        categoria.nombre = nombre
        categoria.descripcion = descripcion
        categoria.save()

        messages.success(request, '¡Categoría actualizada!')
    return redirect('IndexCat')

#Elminar Categoria
def eliminarCategoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    messages.success(request, '¡Categoría eliminada!')
    return redirect('IndexCat')
#/////////////////////////////////////////////////////////////////////////////////////
#Sección Proveedor