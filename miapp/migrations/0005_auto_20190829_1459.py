# Generated by Django 2.1 on 2019-08-29 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0004_auto_20190815_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ejemplar',
            name='fechadecompra',
        ),
        migrations.AddField(
            model_name='ejemplar',
            name='fechadeprestamo',
            field=models.DateField(default=None, verbose_name='Fecha de prestamo'),
            preserve_default=False,
        ),
    ]