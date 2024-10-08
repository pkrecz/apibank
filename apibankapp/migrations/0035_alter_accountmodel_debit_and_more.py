# Generated by Django 5.0.3 on 2024-08-17 14:14

import apibankapp.validators
import django.core.validators
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apibankapp', '0034_alter_accountmodel_free_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountmodel',
            name='debit',
            field=models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='accountmodel',
            name='free_balance',
            field=models.DecimalField(decimal_places=2, max_digits=12, validators=[apibankapp.validators.validator_free_balance]),
        ),
        migrations.AlterField(
            model_name='accountmodel',
            name='percent',
            field=models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
    ]
