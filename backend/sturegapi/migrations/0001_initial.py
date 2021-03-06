# Generated by Django 2.1.2 on 2018-11-03 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StuReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.CharField(max_length=10)),
                ('semester', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('fathername', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('hosteler', models.CharField(max_length=5)),
                ('parentPhone', models.CharField(max_length=15)),
                ('parentEmail', models.CharField(max_length=30)),
                ('permaAddress', models.CharField(max_length=200)),
                ('corresAddress', models.CharField(max_length=200)),
                ('dob', models.DateTimeField()),
            ],
        ),
    ]
