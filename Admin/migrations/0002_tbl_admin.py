# Generated by Django 5.1.4 on 2025-01-07 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Admin_name', models.CharField(max_length=30)),
                ('Admin_Email', models.CharField(max_length=30)),
                ('Admin_Password', models.CharField(max_length=30)),
            ],
        ),
    ]
