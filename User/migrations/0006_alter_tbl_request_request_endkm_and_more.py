# Generated by Django 5.1.4 on 2025-02-11 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_tbl_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_request',
            name='Request_endKm',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tbl_request',
            name='Request_startKm',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
