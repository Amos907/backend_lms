# Generated by Django 3.1.7 on 2021-12-26 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0033_remove_loan_principal'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='principal',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
