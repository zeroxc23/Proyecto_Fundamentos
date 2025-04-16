from django.urls import path
from . import views

urlpatterns = [
    path('IndexInvent/', views.homeinvent, name='IndexInvent'),
    path('IndexInvent/registrarProducto',views.registrarProducto, name="registrarProducto"),
    path('IndexInvent/edicionProducto/<id>',views.edicionProducto),
    path('IndexInvent/editarProducto',views.editarProducto, name="editarProducto"),
    path('IndexInvent/eliminarProducto/<id>',views.eliminarProducto),
]
