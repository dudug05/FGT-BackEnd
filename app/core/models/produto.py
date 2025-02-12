from django.db import models

from .empresa import Empresa

class Produto(models.Model):
    nome_prod = models.CharField(max_length=100)
    preco_prod = models.CharField(max_length=11)
    descricao_prod = models.CharField(max_length=500)
    quantidade_prod = models.DecimalField
    empresa = models.ManyToManyField(Empresa, blank=True)

def __str__(self):
        return f"{self.nome_prod} - {self.preco_prod} - {self.descricao_prod} - {self.quantidade_prod} - {self.empresa}"