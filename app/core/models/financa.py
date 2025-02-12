from django.db import models

from .empresa import Empresa
from .cliente import Cliente


class Financa(models.Model):
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    valor = models.CharField(max_length=11)
    cliente = models.ManyToManyField(Cliente, blank=True)
    empresa = models.ManyToManyField(Empresa, blank=True)


def __str__(self):
        return f"{self.tipo} - {self.valor} - {self.descricao} - {self.cliente}"