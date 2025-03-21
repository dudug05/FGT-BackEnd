# Generated by Django 5.1.6 on 2025-03-20 18:02

import core.models.user
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0017_alter_budget_date_budget_alter_product_price_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(help_text='Email', max_length=255, unique=True, verbose_name='email')),
                ('name', models.CharField(blank=True, help_text='Username', max_length=255, null=True, verbose_name='name')),
                ('is_active', models.BooleanField(default=True, help_text='Indica que este usuário está ativo.', verbose_name='Usuário está ativo')),
                ('is_staff', models.BooleanField(default=False, help_text='Indica que este usuário pode acessar o Admin.', verbose_name='Usuário é da equipe')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='custom_user_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_permissions_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', core.models.user.UserManager()),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
