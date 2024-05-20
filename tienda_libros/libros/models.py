from django.db import models

# Create your models here.
# libros/models.py

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        db_table = 'libro'
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.titulo
