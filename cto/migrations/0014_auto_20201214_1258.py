# Generated by Django 3.0.7 on 2020-12-14 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cto', '0013_auto_20201210_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipocontrato',
            name='enCalidadDe2e',
            field=models.CharField(default='', max_length=150, verbose_name='En calidad de 2'),
        ),
        migrations.AddField(
            model_name='tipocontrato',
            name='enCalidadDe2f',
            field=models.CharField(default='', max_length=150, verbose_name='En calidad de 2'),
        ),
    ]
