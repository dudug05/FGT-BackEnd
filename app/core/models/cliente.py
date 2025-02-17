from django.db import models

from .fornecedor import Fornecedor


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=500)
    fornecedor = models.ForeignKey(
        Fornecedor, on_delete=models.PROTECT, related_name="fornecedor", null=True, blank=True
    )

def __str__(self):
        return f"{self.nome} - {self.telefone} - {self.fornecedor}"