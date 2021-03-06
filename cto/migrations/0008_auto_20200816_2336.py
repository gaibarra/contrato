# Generated by Django 3.0.7 on 2020-08-17 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cto', '0007_doctos_pdf2'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='direccion',
            field=models.IntegerField(blank=True, null=True, verbose_name='Dirección'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='rango1',
            field=models.IntegerField(blank=True, null=True, verbose_name='Rango inicial'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='rango2',
            field=models.IntegerField(blank=True, null=True, verbose_name='Rango final'),
        ),
    ]
