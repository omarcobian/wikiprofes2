# Generated by Django 5.1.3 on 2024-11-23 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=80)),
                ('departamento', models.CharField(max_length=50)),
            ],
        ),
    ]
