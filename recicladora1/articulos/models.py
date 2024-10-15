# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Articulos(models.Model):
    CATEGORIAS = [
        ('latas', 'Latas'),
        ('botellas', 'Botellas'),
        ('cajas_de_botellas', 'Cajas de Botellas'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    cantidad = models.PositiveIntegerField(default=0)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fecha_registro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.categoria} - {self.cantidad} unidades - {self.valor} valor"
