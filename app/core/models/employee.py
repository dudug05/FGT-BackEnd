from django.db import models
from django.core.validators import RegexValidator


class Employee(models.Model):
    name_employee = models.CharField(max_length=100)
    cpf_employee = models.CharField(
        max_length=14,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                regex=r"^\d{3}\.\d{3}\.\d{3}-\d{2}$",
                message="O CPF deve estar no formato 000.000.000-00",
                code="invalid_cpf",
            )
        ],
    )

    email_employee = models.EmailField(blank=True, null=True)
    job_employee = models.CharField(max_length=100)

    salary_employee = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    accountNumber_employee = models.CharField(max_length=20, blank=True, null=True)
    agency_employee = models.CharField(max_length=6, blank=True, null=True)

    admissionDate_employee = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name_employee} - {self.cpf_employee} - {self.email_employee} - {self.job_employee} - {self.salary_employee} - {self.accountNumber_employee} - {self.agency_employee} - {self.admissionDate_employee}"
