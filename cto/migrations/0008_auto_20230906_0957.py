# Generated by Django 3.2.9 on 2023-09-06 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cto', '0007_auto_20230313_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='contratos',
            name='clausula',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='contratos',
            name='testimonio',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
    ]
