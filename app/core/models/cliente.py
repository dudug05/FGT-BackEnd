from django.db import models

from .empresa import Empresa


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=500)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, related_name="empresa", null=True, blank=True
    )

def __str__(self):
        return f"{self.nome} - {self.telefone} - {self.empresa}"