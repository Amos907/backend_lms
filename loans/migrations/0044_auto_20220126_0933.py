# Generated by Django 3.1.7 on 2022-01-26 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0043_auto_20220126_0903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='loan_id',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='loan',
            name='user',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
