# Generated by Django 3.1.7 on 2022-02-11 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa_payments', '0008_paymentstoday_loan_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='overduepayments',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
