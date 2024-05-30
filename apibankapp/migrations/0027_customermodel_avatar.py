# Generated by Django 5.0.3 on 2024-05-30 08:48

import apibankapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apibankapp', '0026_alter_operationmodel_balance_after_operation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermodel',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=apibankapp.models.CustomerModel.get_upload_path),
        ),
    ]