# Generated by Django 2.1 on 2019-08-29 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0005_auto_20190829_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ejemplar',
            name='fechadeprestamo',
        ),
        migrations.AddField(
            model_name='ejemplar',
            name='fechadeentrega',
            field=models.DateField(default=None, verbose_name='Fecha de entrega'),
            preserve_default=False,
        ),
    ]
