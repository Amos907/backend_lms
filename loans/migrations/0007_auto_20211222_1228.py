# Generated by Django 3.1.7 on 2021-12-22 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0006_auto_20211222_1227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='loan_type_id',
            new_name='loan_type_name',
        ),
    ]
