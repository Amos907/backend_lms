# Generated by Django 3.1.7 on 2022-02-11 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0051_auto_20220211_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='amount_due',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
    ]
