# Generated by Django 5.0.3 on 2024-05-16 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apibankapp', '0023_alter_accountmodel_balance_alter_accountmodel_debit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountmodel',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='accountmodel',
            name='created_employee',
            field=models.CharField(max_length=50),
        ),
    ]
