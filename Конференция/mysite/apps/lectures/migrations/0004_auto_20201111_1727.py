# Generated by Django 3.0.6 on 2020-11-11 12:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0003_auto_20201110_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 11, 12, 27, 3, 162490, tzinfo=utc), verbose_name='Время конца доклада'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 11, 12, 27, 3, 162490, tzinfo=utc), verbose_name='Время начала доклада'),
        ),
    ]
