from django.db import models

from .pedido import Pedido
from .produto import Produto
from .servico import Servico


class ItemPedido(models.Model):
    quantidade = models.CharField(max_length=10)
    preco_uni = models.CharField(max_length=11)
    pedido = models.ManyToManyField(Pedido, blank=True)
    produto = models.ManyToManyField(Produto, blank=True)
    servico = models.ManyToManyField(Servico, blank=True)


def __str__(self):
        return f"{self.quantidade} - {self.preco_uni} - {self.pedido} - {self.produto} - {self.servico}"