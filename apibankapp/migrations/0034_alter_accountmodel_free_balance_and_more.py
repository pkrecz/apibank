# Generated by Django 5.0.3 on 2024-08-13 16:04

import apibankapp.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apibankapp', '0033_logmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountmodel',
            name='free_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, validators=[apibankapp.validators.validator_free_balance]),
        ),
        migrations.AlterField(
            model_name='accountmodel',
            name='number_iban',
            field=models.CharField(blank=True, max_length=28, validators=[apibankapp.validators.validator_number_iban]),
        ),
    ]
