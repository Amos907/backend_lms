# Generated by Django 3.1.7 on 2022-02-19 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0054_auto_20220211_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='total_balance',
            field=models.IntegerField(default=0),
        ),
    ]
