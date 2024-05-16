# Generated by Django 5.0.3 on 2024-05-16 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apibankapp', '0012_rename_created_date_customermodel_created_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountmodel',
            old_name='Account_type',
            new_name='account_type',
        ),
        migrations.RenameField(
            model_name='accountmodel',
            old_name='Balance',
            new_name='balance',
        ),
        migrations.RenameField(
            model_name='accountmodel',
            old_name='Created_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='accountmodel',
            old_name='Created_employee',
            new_name='created_employee',
        ),
        migrations.RenameField(
            model_name='accountmodel',
            old_name='Customer',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='accountmodel',
            old_name='Debit',
            new_name='debit',
        ),
        migrations.RenameField(
            model_name='accountmodel',
            old_name='Free_balance',
            new_name='free_balance',
        ),
        migrations.RenameField(
            model_name='accountmodel',
            old_name='Id_account',
            new_name='id_account',
        ),
        migrations.RenameField(
            model_name='accountmodel',
            old_name='Number_IBAN',
            new_name='number_IBAN',
        ),
        migrations.RenameField(
            model_name='accountmodel',
            old_name='Percent',
            new_name='percent',
        ),
    ]
