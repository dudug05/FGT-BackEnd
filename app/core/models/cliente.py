from django.db import models


class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField(default="exemplo@email.com")
    telefone_cliente = models.CharField(max_length=11)
    endereco_cliente = models.CharField(max_length=500)

def __str__(self):
        return f"{self.nome_cliente} - {self.telefone_cliente} - {self.email_cliente} - {self.endereco_cliente}"