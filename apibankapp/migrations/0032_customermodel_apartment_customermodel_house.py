# Generated by Django 5.0.3 on 2024-08-02 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apibankapp', '0031_rename_address_customermodel_street'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermodel',
            name='apartment',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='customermodel',
            name='house',
            field=models.CharField(default='25', max_length=10),
            preserve_default=False,
        ),
    ]
