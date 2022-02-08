# Generated by Django 3.1.7 on 2022-01-26 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0046_auto_20220126_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='loan_type',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='principal',
        ),
        migrations.RemoveField(
            model_name='loantype',
            name='description',
        ),
        migrations.RemoveField(
            model_name='loantype',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='loantype',
            name='interest_rate',
        ),
        migrations.RemoveField(
            model_name='loantype',
            name='loan_type_name',
        ),
        migrations.RemoveField(
            model_name='loantype',
            name='min_collateral',
        ),
        migrations.AddField(
            model_name='loan',
            name='loan_amount',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='loantype',
            name='eight_weeks',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='loantype',
            name='five_weeks',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='loantype',
            name='four_weeks',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='loantype',
            name='loan_amount',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='loantype',
            name='seven_weeks',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='loantype',
            name='ten_weeks',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]