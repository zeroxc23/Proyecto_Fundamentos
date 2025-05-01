from django.urls import path
from . import views

urlpatterns = [
    #Inventario/Producto
    path('IndexInvent/', views.homeinvent, name='IndexInvent'),
    path('IndexInvent/registrarProducto',views.registrarProducto, name="registrarProducto"),
    path('IndexInvent/edicionProducto/<id>',views.edicionProducto),
    path('IndexInvent/editarProducto',views.editarProducto, name="editarProducto"),
    path('IndexInvent/eliminarProducto/<id>',views.eliminarProducto),
    #Categoria
    path('IndexCat/', views.homecategoria, name='IndexCat'),
    path('IndexCat/registrarCategoria',views.registrarCategoria, name='registrarCategoria'),
    path('IndexCat/edicionCategoria/<id>',views.edicionCategoria),
    path('IndexCat/editarCategoria',views.editarCategoria, name="editarCategoria"),
    path('IndexCat/eliminarCategoria/<id>',views.eliminarCategoria),
    #Proveedor
    path('IndexProv/', views.homeproveedor, name='IndexProv'),
    path('IndexProv/registrarProveedor',views.registrarProveedor, name='registrarProveedor'),
    path('IndexProv/edicionProveedor/<id>',views.edicionProveedor),
    path('IndexProv/editarProveedor', views.editarProveedor, name="editarProveedor"),
    path('IndexProv/eliminarProveedor/<id>',views.eliminarProveedor),
    #Inventario/productoIusuario
    path('IndexUsuProducto/', views.homeusuinevnt, name='IndexUsuProducto'),
    path('IndexUsuProducto/edicionProducto/<id>', views.edicionusuProducto),
    path('IndexUsuProducto/editarProducto', views.editarusuProducto, name='editarusuProducto'),
    path('IndexUsuProducto/eliminarProducto/<id>', views.eliminarusuProducto),
    #Usuario Categoria
    path('IndexUsuCategoria/', views.homeusucategoria, name='IndexUsuCategoria'),
    path('IndexUsuCategoria/edicionCategoria/<id>', views.edicionusucategoria),
    path('IndexUsuCategoria/editarCategoria', views.editarusucategoria, name='editarcategoriausu'),
    path('IndexUsuCategoria/eliminarCategoria/<id>', views.eliminarusucategoria),

    #Usuario Proveedor
    path('IndexUsuProveedor/', views.homeusuproveedor, name='IndexUsuProveedor'),
    path('IndexUsuProveedor/edicionProveedor/<id>', views.edicionusuproveedor),
    path('IndexUsuProveedor/editarProveedor', views.editarusuproveedor, name='editarproveedorusu'),
    path('IndexUsuProveedor/eliminarProveedor/<id>', views.eliminarusuproveedor),
]
