# Generated by Django 2.2.5 on 2020-09-20 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
