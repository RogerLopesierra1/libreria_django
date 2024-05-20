from django.shortcuts import render
from .models import Libro

# Create your views here.
# libros/views.py

def index(request):
    return render(request, 'index.html')

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/lista_libros.html', {'libros': libros})