from django.db import models

from .empresa import Empresa

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    preco = models.CharField(max_length=11)
    empresa = models.ManyToManyField(Empresa, blank=True)



def __str__(self):
        return f"{self.nome} - {self.descricao} - {self.preco}"