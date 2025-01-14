# Generated by Django 5.0.6 on 2024-05-29 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_alter_libro_options_alter_libro_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('contraseña', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuario',
            },
        ),
    ]
