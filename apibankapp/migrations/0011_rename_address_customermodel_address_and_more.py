# Generated by Django 5.0.3 on 2024-05-16 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apibankapp', '0010_rename_id_customer_customermodel_id_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customermodel',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='customermodel',
            old_name='Birth_city',
            new_name='birth_city',
        ),
        migrations.RenameField(
            model_name='customermodel',
            old_name='Birth_date',
            new_name='birth_date',
        ),
        migrations.RenameField(
            model_name='customermodel',
            old_name='City',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='customermodel',
            old_name='First_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customermodel',
            old_name='Identification',
            new_name='identification',
        ),
        migrations.RenameField(
            model_name='customermodel',
            old_name='Last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='customermodel',
            old_name='Pesel',
            new_name='pesel',
        ),
        migrations.RenameField(
            model_name='customermodel',
            old_name='Postal_code',
            new_name='postal_code',
        ),
    ]
