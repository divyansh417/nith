# Generated by Django 2.1.2 on 2018-10-30 06:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrationapi', '0002_reg_p1enddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg',
            name='p1EndDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 30, 6, 30, 28, 657182)),
        ),
    ]
