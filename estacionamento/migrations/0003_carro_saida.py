# Generated by Django 2.2.7 on 2019-11-29 01:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamento', '0002_auto_20191126_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='saida',
            field=models.DateField(default=datetime.datetime(2019, 11, 29, 1, 14, 27, 877191, tzinfo=utc), verbose_name='Saida'),
            preserve_default=False,
        ),
    ]