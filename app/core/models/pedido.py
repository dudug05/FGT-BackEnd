from django.db import models

from .empresa import Empresa
from .cliente import Cliente


class Pedido(models.Model):
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    cliente = models.ManyToManyField(Cliente, blank=True)
    empresa = models.ManyToManyField(Empresa, blank=True)

def __str__(self):
        return f"{self.total} - {self.descricao} - {self.cliente} - {self.empresa}"