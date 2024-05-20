from django.contrib import admin
from .models import Libro

# Register your models here.
class LibroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'fecha_publicacion', 'isbn', 'precio')

admin.site.register(Libro, LibroAdmin)