# Generated by Django 2.2.5 on 2020-09-20 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TenderPost', '0001_initial'),
        ('User', '0003_auto_20200919_2258'),
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenderbid',
            name='tender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.Tender'),
        ),
        migrations.AddField(
            model_name='tenderbid',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Profile'),
        ),
    ]
