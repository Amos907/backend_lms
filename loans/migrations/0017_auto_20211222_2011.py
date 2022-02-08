# Generated by Django 3.1.7 on 2021-12-22 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0016_auto_20211222_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loan_type_name',
            field=models.CharField(choices=[('Personal Loan', 'Personal Loan'), ('Small Business Loan', 'Small Business Loan'), ('Mortgate', 'Mortgate')], default='Personal Loan', max_length=200),
        ),
    ]