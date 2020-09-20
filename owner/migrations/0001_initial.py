# Generated by Django 2.2.5 on 2020-09-20 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0003_auto_20200919_2258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tender_title', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('category', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('publish_date', models.DateField()),
                ('closing_date', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PD', 'Pending'), ('SC', 'Successful')], default='PD', max_length=2)),
                ('tender', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='owner.Tender')),
            ],
        ),
    ]
