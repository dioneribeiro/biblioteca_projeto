# Generated by Django 5.1 on 2024-08-17 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0011_livros_sinopse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='sinopse',
            field=models.TextField(blank=True, null=True),
        ),
    ]
