# Generated by Django 3.1.7 on 2022-02-11 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0053_auto_20220211_0923'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='amount_due',
            new_name='overdue_amount',
        ),
    ]
