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
]
