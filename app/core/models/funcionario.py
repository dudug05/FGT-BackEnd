from django.db import models


class Funcionario(models.Model):
    nome_func = models.CharField(max_length=100)
    funcao_func = models.CharField(max_length=100)
    salario_func = models.DecimalField(max_digits=10, decimal_places=2)
    data_admissao_func = models.DateField(null=True, blank=True)


def __str__(self):
        return f"{self.nome} - {self.funcao_func} - {self.salario_func} - {self.data_admissao_func}"