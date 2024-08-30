from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='listar'),
    path('agregar/', views.agregar, name='agregar'),
    path('editar/<int:prenda_id>', views.editar, name='editar'),
    path('eliminar/<int:prenda_id>', views.eliminar, name='eliminar'),
]
