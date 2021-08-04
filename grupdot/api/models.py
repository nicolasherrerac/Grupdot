from django.db import models

# Create your models here.

class cotizacion(models.Model):
    """Modelo de la base de datos"""
    name = models.CharField(max_length=255, null=True)
    tasa = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    monto = models.PositiveIntegerField()
