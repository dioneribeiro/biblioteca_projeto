# Generated by Django 5.1.1 on 2024-10-04 01:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0029_remove_livros_nome_emprestado_and_more'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario'),
            preserve_default=False,
        ),
    ]
