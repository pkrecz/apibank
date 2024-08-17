# Generated by Django 5.0.3 on 2024-08-17 15:03

import django.core.validators
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apibankapp', '0036_alter_operationmodel_value_operation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounttypemodel',
            name='percent',
            field=models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
    ]
