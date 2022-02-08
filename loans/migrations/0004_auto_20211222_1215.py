# Generated by Django 3.1.7 on 2021-12-22 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0003_auto_20211222_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan_type',
            name='loan_type_name',
            field=models.CharField(choices=[('SB', 'Small Business Loan'), ('M', 'Mortgage Loan'), ('P', 'Personal_Loan')], default='P', max_length=2),
        ),
    ]