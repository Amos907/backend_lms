# Generated by Django 3.1.7 on 2022-02-06 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa_payments', '0006_auto_20220205_0658'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentsToday',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.CharField(blank=True, max_length=200, null=True)),
                ('installment', models.CharField(blank=True, max_length=200, null=True)),
                ('week', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]