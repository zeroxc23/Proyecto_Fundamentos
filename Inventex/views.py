from django.shortcuts import render, redirect

# Pagina Principal
def index(request):
    message = "Bienvenido a Inventex"
    return render(request, 'index.html')