# Generated by Django 3.1.7 on 2021-12-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0036_auto_20211226_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]