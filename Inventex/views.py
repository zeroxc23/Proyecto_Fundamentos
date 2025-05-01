from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import logout_required
from django.contrib.auth.models import User

# Página Principal
def index(request):
    return render(request, 'index.html')

# Redirección Usuario
def indexUsu(request):
    if not request.user.is_authenticated:
        return redirect('login')  
    if request.user.is_staff:
        return redirect('acceso_denegado')  
    
    username = request.user.username
    message = f"Bienvenido a Inventex, {username}"
    return render(request, "IndexUsu.html", {'message': message})

# Login
def login(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            request.session['username'] = user.username  
            if user.is_staff:  
                return redirect('indexAdmin')
            else:
                return redirect('indexUsu')
        else:
            return render(request, 'Login.html', {'error_message': 'Nombre de usuario o contraseña incorrectos.'})
    else:
        return render(request, 'Login.html')

# Acceso Errores
def acceso_denegado(request):
    return render(request, 'AccesoDenegado.html')

# Redirección Administrador
@login_required
def indexAdmin(request):
    if not request.user.is_staff:
        return redirect('acceso_denegado')  
    username = request.user.username
    message = f"Bienvenido Administrador, {username}"
    return render(request, "IndexAdmin.html", {'message': message})

# Logout
@logout_required
def logout_view(request):
    logout(request)
    return redirect('Index')

# Registrarse
def register(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('contraseña')
        
        if User.objects.filter(username=usuario).exists():
            return render(request, 'Register.html', {'error_message': 'El nombre de usuario ya está en uso.'})
        
        user = User.objects.create_user(username=usuario, email=correo, password=contraseña)
        user.first_name = nombre
        user.last_name = apellido
        user.save()

        user = authenticate(username=usuario, password=contraseña)
        if user is not None:
            auth_login(request, user)
            return redirect('Index')
        else:
            return render(request, 'Register.html', {'error_message': 'Hubo un problema al autenticar el usuario.'})

    return render(request, 'Register.html')
