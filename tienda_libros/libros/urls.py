from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('libros/', views.lista_libros, name='lista_libros'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
]
