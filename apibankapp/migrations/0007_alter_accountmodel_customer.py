# Generated by Django 5.0.3 on 2024-05-07 19:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apibankapp', '0006_rename_fk_id_customer_accountmodel_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountmodel',
            name='Customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apibankapp.customermodel'),
        ),
    ]
