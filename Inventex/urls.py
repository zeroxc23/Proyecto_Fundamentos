"""
URL configuration for Inventex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Inventex import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #Pagina Principal
    path('', views.index, name="Index"),
    #Aplicación
    path('Inventario/',include('Aplicacion.Inventario.urls')),
    # Credenciales
    path('login/', views.login, name='Login'),
    path('indexadmin/', views.indexAdmin, name='indexAdmin'),
    path('indexusu/', views.indexUsu, name='indexUsu'),
    path('logout/', views.logout_view, name='Logout'),
    path('register/', views.register, name='Register'),
    #Accesos
    path('acceso-denegado/', views.acceso_denegado, name='acceso_denegado'),

]
