# Generated by Django 2.1.2 on 2018-11-03 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrationapi', '0007_auto_20181103_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg',
            name='p1EndDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 3, 16, 43, 1, 620655)),
        ),
    ]
