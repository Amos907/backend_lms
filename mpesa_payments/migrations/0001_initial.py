# Generated by Django 3.1.7 on 2022-01-31 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MpesaPayment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mpesa', models.CharField(blank=True, max_length=200, null=True)),
                ('full_name', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('phone_number', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]