from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Proveedor, Producto
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#/////////////////////////////////////////////////////////////////////////////////////
# Administrador
# Sección Inventario

# Página de Inventario
@login_required
def homeinvent(request):
    if not request.user.is_staff:
        return redirect('acceso_denegado')

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
@login_required
def registrarProducto(request):
    if not request.user.is_staff:
        return redirect('acceso_denegado')

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
@login_required
def edicionProducto(request, id):
    if not request.user.is_staff:
        return redirect('acceso_denegado')

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
@login_required
def editarProducto(request):
    if not request.user.is_staff:
        return redirect('acceso_denegado')

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
@login_required
def eliminarProducto(request, id):
    if not request.user.is_staff:
        return redirect('acceso_denegado')

    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, '¡Producto eliminado!')
    return redirect('IndexInvent')

#/////////////////////////////////////////////////////////////////////////////////////
# Sección Categoria
@login_required
def homecategoria(request):
    if not request.user.is_staff:
        return redirect('acceso_denegado')

    categorias = Categoria.objects.all()
    messages.success(request, '¡Categoria listada!')
    return render(request, "gestionCategoria.html", {
        "categorias": categorias,
    })

@login_required
def registrarCategoria(request):
    if not request.user.is_staff:
        return redirect('acceso_denegado')

    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        descripcion = request.POST['txtDescripcion']
        Categoria.objects.create(
            nombre=nombre,
            descripcion=descripcion
        )
        messages.success(request, '¡Categoría registrada!')
    return redirect('IndexCat')

@login_required
def edicionCategoria(request, id):
    if not request.user.is_staff:
        return redirect('acceso_denegado')

    categorias = get_object_or_404(Categoria, id=id)
    return render(request, "editarCategoria.html", {
        "categorias": categorias,
    })

@login_required
def editarCategoria(request):
    if not request.user.is_staff:
        return redirect('acceso_denegado')

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

@login_required
def eliminarCategoria(request, id):
    if not request.user.is_staff:
        return redirect('acceso_denegado')

    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    messages.success(request, '¡Categoría eliminada!')
    return redirect('IndexCat')

#/////////////////////////////////////////////////////////////////////////////////////
# Sección Proveedor
@login_required
def homeproveedor(request):
    if not request.user.is_staff:
        return redirect('acceso_denegado')

    proveedor = Proveedor.objects.all()
    messages.success(request, '¡Proveedor listado!')
    return render(request, "gestionProveedor.html", {
        "proveedor": proveedor,
    })

@login_required
def registrarProveedor(request):
    if not request.user.is_staff:
        return redirect('acceso_denegado')

    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        direccion = request.POST['txtDireccion']
        correo = request.POST['txtCorreo']
        telefono = request.POST['txtTelefono']
        Proveedor.objects.create(
            nombre=nombre,
            direccion=direccion,
            correo=correo,
            telefono=telefono
        )
        messages.success(request, '¡Proveedor resgitrado!')
    return redirect('IndexProv')

@login_required
def edicionProveedor(request, id):
    if not request.user.is_staff:
        return redirect('acceso_denegado')

    proveedor = get_object_or_404(Proveedor, id=id)
    return render(request, "editarProveedor.html", {
        "proveedor": proveedor,
    })

@login_required
def editarProveedor(request):
    if not request.user.is_staff:
        return redirect('acceso_denegado')

    if request.method == 'POST':
        id = request.POST['txtId']
        nombre = request.POST['txtNombre']
        direccion = request.POST['txtDireccion']
        correo = request.POST['txtCorreo']
        telefono = request.POST['txtTelefono']
        proveedor = get_object_or_404(Proveedor, id=id)
        proveedor.nombre = nombre
        proveedor.direccion = direccion
        proveedor.correo = correo
        proveedor.telefono = telefono
        proveedor.save()
        messages.success(request, '¡Proveedor actualizado!')
    return redirect('IndexProv')

@login_required
def eliminarProveedor(request, id):
    if not request.user.is_staff:
        return redirect('acceso_denegado')

    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.delete()
    messages.success(request, '¡Proveedor eliminado!')
    return redirect('IndexProv')

#/////////////////////////////////////////////////////////////////////////////////////
# Usuario
# Sección Inventario
@login_required
def homeusuinevnt(request):
    if request.user.is_staff:
        return redirect('acceso_denegado')

    productos_listados = Producto.objects.all()
    return render(request, "gestionusuProducto.html", {
        "productos": productos_listados,
    })

@login_required
def edicionusuProducto(request, id):
    if request.user.is_staff:
        return redirect('acceso_denegado')

    producto = get_object_or_404(Producto, id=id)
    producto.precio = str(producto.precio)
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()
    return render(request, "editarUsuProducto.html", {
        "producto": producto,
        "categorias": categorias,
        "proveedores": proveedores
    })

@login_required
def editarusuProducto(request):
    if request.user.is_staff:
        return redirect('acceso_denegado')

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
    return redirect('IndexUsuProducto')

@login_required
def eliminarusuProducto(request, id):
    if request.user.is_staff:
        return redirect('acceso_denegado')

    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, '¡Producto eliminado!')
    return redirect('IndexUsuProducto')

#/////////////////////////////////////////////////////////////////////////////////////
# Sección Categoria
@login_required
def homeusucategoria(request):
    if request.user.is_staff:
        return redirect('acceso_denegado')

    categorias = Categoria.objects.all()
    return render(request, "gestionUsuCategoria.html", {
        "categorias": categorias,
    })

@login_required
def edicionusucategoria(request, id):
    if request.user.is_staff:
        return redirect('acceso_denegado')

    categoria = get_object_or_404(Categoria, id=id)
    return render(request, "editarUsuCategoria.html", {
        "categoria": categoria,
    })

@login_required
def editarusucategoria(request):
    if request.user.is_staff:
        return redirect('acceso_denegado')

    if request.method == 'POST':
        id = request.POST['txtId']
        nombre = request.POST['txtNombre']
        descripcion = request.POST['txtDescripcion']
        categoria = get_object_or_404(Categoria, id=id)
        categoria.nombre = nombre
        categoria.descripcion = descripcion
        categoria.save()
        messages.success(request, '¡Categoría actualizada!')
    return redirect('IndexUsuCategoria')

@login_required
def eliminarusucategoria(request, id):
    if request.user.is_staff:
        return redirect('acceso_denegado')

    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    messages.success(request, '¡Categoría eliminada!')
    return redirect('IndexUsuCategoria')

#/////////////////////////////////////////////////////////////////////////////////////
# Sección Proveedor
@login_required
def homeusuproveedor(request):
    if request.user.is_staff:
        return redirect('acceso_denegado')

    proveedores = Proveedor.objects.all()
    return render(request, "gestionUsuProveedor.html", {
        "proveedores": proveedores,
    })

@login_required
def edicionusuproveedor(request, id):
    if request.user.is_staff:
        return redirect('acceso_denegado')

    proveedor = get_object_or_404(Proveedor, id=id)
    return render(request, "editarUsuProveedor.html", {
        "proveedor": proveedor,
    })

@login_required
def editarusuproveedor(request):
    if request.user.is_staff:
        return redirect('acceso_denegado')

    if request.method == 'POST':
        id = request.POST['txtId']
        nombre = request.POST['txtNombre']
        direccion = request.POST['txtDireccion']
        correo = request.POST['txtCorreo']
        telefono = request.POST['txtTelefono']
        proveedor = get_object_or_404(Proveedor, id=id)
        proveedor.nombre = nombre
        proveedor.direccion = direccion
        proveedor.correo = correo
        proveedor.telefono = telefono
        proveedor.save()
        messages.success(request, '¡Proveedor actualizado!')
    return redirect('IndexUsuProveedor')

@login_required
def eliminarusuproveedor(request, id):
    if request.user.is_staff:
        return redirect('acceso_denegado')

    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.delete()
    messages.success(request, '¡Proveedor eliminado!')
    return redirect('IndexUsuProveedor')
