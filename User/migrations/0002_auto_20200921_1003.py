# Generated by Django 2.2.5 on 2020-09-21 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='registration_num',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
