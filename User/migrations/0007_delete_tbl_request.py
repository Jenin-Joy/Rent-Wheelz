# Generated by Django 5.1.4 on 2025-02-18 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_alter_tbl_request_request_endkm_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_Request',
        ),
    ]
