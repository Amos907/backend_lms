# Generated by Django 3.1.7 on 2021-12-26 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0034_auto_20211226_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='date_created',
            field=models.DateField(),
        ),
    ]
