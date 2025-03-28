# Generated by Django 5.1.6 on 2025-03-19 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_supplier"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.RemoveField(
            model_name="service",
            name="product",
        ),
        migrations.AddField(
            model_name="service",
            name="product",
            field=models.ManyToManyField(
                related_name="Service_product", to="core.product"
            ),
        ),
    ]
