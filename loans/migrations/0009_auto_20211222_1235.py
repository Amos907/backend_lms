# Generated by Django 3.1.7 on 2021-12-22 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0008_auto_20211222_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan_type',
            name='duration',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='loan_type',
            name='intereset_rate',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='loan_type',
            name='penalty_rate',
            field=models.IntegerField(blank=True, default=True, null=True),
        ),
    ]