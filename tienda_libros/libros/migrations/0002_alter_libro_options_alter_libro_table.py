# Generated by Django 5.0.6 on 2024-05-20 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='libro',
            options={'verbose_name': 'Libro', 'verbose_name_plural': 'Libros'},
        ),
        migrations.AlterModelTable(
            name='libro',
            table='libro',
        ),
    ]
