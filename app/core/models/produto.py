from django.db import models

from .fornecedor import Fornecedor

class Produto(models.Model):
    nome_prod = models.CharField(max_length=100)
    preco_prod = models.CharField(max_length=11)
    descricao_prod = models.CharField(max_length=500)
    quantidade_prod = models.DecimalField
    fornecedor = models.ManyToManyField(Fornecedor, blank=True)

def __str__(self):
        return f"{self.nome_prod} - {self.preco_prod} - {self.descricao_prod} - {self.quantidade_prod} - {self.fornecedor}"