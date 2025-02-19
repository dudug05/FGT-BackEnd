from django.db import models

from .cliente import Cliente
from .servico import Servico
from .orcamento import Orcamento

class OrdemServico(models.Model):
    codigo_os = models.AutoField(primary_key=True)
    data_os = models.DateField(null=False)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.PROTECT, related_name="clientes_cli", null=True, blank=True
    )
    orcamento = models.ForeignKey(
        Orcamento,on_delete=models.PROTECT, related_name="orcamento", null=True, blank=True
    )
    servico = models.ManyToManyField(Servico, blank=True)

def __str__(self):
    return f"{self.codigo_os} - {self.data_os} - {self.cliente} - {self.orcamento} - {self.servico}"

