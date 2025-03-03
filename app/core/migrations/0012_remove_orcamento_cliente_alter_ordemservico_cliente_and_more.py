# Generated by Django 5.1.6 on 2025-02-19 21:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_remove_orcamento_endereco_orca"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orcamento",
            name="cliente",
        ),
        migrations.AlterField(
            model_name="ordemservico",
            name="cliente",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="clientes_cli",
                to="core.cliente",
            ),
        ),
        migrations.RemoveField(
            model_name="servico",
            name="cliente",
        ),
        migrations.AddField(
            model_name="orcamento",
            name="cliente",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="clientes_orca",
                to="core.cliente",
            ),
        ),
        migrations.AddField(
            model_name="servico",
            name="cliente",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="clientes_ser",
                to="core.cliente",
            ),
        ),
    ]
