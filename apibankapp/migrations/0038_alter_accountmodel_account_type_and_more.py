# Generated by Django 5.0.3 on 2024-11-01 15:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apibankapp', '0037_alter_accounttypemodel_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountmodel',
            name='account_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='accounttype_accounts', to='apibankapp.accounttypemodel'),
        ),
        migrations.AlterField(
            model_name='accountmodel',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customer_accounts', to='apibankapp.customermodel'),
        ),
        migrations.AlterField(
            model_name='operationmodel',
            name='id_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='account_operations', to='apibankapp.accountmodel'),
        ),
    ]
