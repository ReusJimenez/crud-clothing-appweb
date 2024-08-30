from django.db import models

# Create your models here.

class Prenda(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    talla = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)
    marca = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    precio = models.FloatField()
    cantidad = models.IntegerField()

    class Meta:
        db_table = "prenda"
