from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)


class Catalogo(models.Model):
    fecha_creacion = models.DateField(verbose_name='Fecha de creacion')
    admin_creador = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Catalogos"