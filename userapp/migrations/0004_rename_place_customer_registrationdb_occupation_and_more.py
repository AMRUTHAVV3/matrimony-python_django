# Generated by Django 4.2 on 2023-07-21 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_customer_registrationdb_password_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer_registrationdb',
            old_name='place',
            new_name='occupation',
        ),
        migrations.RemoveField(
            model_name='customer_registrationdb',
            name='streetnr',
        ),
        migrations.RemoveField(
            model_name='customer_registrationdb',
            name='zipcode',
        ),
    ]
