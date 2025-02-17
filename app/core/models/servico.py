from django.db import models

from .cliente import Cliente

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    preco = models.CharField(max_length=11)
    cliente = models.ManyToManyField(Cliente, blank=True)



def __str__(self):
        return f"{self.nome} - {self.descricao} - {self.preco}"