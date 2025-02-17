from django.db import models


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)

def __str__(self):
        return f"{self.nome} - {self.descricao} - {self.setor}"