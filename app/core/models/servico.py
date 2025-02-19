from django.db import models

from .cliente import Cliente
from .produto import Produto

class Servico(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.PROTECT, related_name="clientes_ser", null=True, blank=True
    )
    data_emissao = models.DateField(null=True, blank=True)
    data_entrega = models.DateField(null=True, blank=True)
    tipo_servico = models.CharField(max_length=100)
    produto_utilizado = models.ManyToManyField(Produto, blank=True)




def __str__(self):
        return f"{self.cliente} - {self.data_entrega} - {self.data_emissao} - {self.tipo_servico} - {self.produto_utilizado}"