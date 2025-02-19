from django.db import models

from .cliente import Cliente
from .produto import Produto
from .servico import Servico

class Orcamento(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.PROTECT, related_name="clientes_orca", null=True, blank=True
    )
    data_orca = models.DateField()
    produto = models.ManyToManyField(Produto, blank=True)
    servico =  models.ForeignKey(
        Servico, on_delete=models.PROTECT, related_name="servico", null=True, blank=True
    )
    preco_orca = models.DecimalField(max_digits=10, decimal_places=2)

    def total(self):

        return sum([produto.preco_prod for produto in self.produto.all()])

    def __str__(self):
        produtos = ", ".join([str(produto) for produto in self.produto.all()])
        return f'Orçamento {self.id}: {self.cliente} - {self.data_orca} - {self.servico} - {self.produto} '
