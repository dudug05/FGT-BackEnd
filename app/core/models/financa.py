from django.db import models

from .fornecedor import Fornecedor
from .cliente import Cliente


class Financa(models.Model):
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    valor = models.CharField(max_length=11)
    cliente = models.ManyToManyField(Cliente, blank=True)
    Fornecedor = models.ManyToManyField(Fornecedor, blank=True)


def __str__(self):
        return f"{self.tipo} - {self.valor} - {self.descricao} - {self.cliente}"