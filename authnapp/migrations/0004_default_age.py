# Generated by Django 2.2.16 on 2020-11-13 09:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0003_default_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 9, 32, 22, 471333, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
