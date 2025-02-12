from django.db import models

from .usuario import Usuario


class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    Usuario = models.ForeignKey(
        Usuario, on_delete=models.PROTECT, related_name="usuario", null=True, blank=True
    )

def __str__(self):
        return f"{self.nome} - {self.descricao} - {self.setor}"