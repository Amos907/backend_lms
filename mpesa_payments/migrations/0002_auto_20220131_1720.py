# Generated by Django 3.1.7 on 2022-01-31 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa_payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='B2CMpesaPayment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mpesa', models.CharField(blank=True, max_length=200, null=True)),
                ('full_name', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('phone_number', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='C2BMpesaPayment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mpesa', models.CharField(blank=True, max_length=200, null=True)),
                ('full_name', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('phone_number', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='MpesaPayment',
        ),
    ]
