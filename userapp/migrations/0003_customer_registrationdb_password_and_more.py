# Generated by Django 4.2 on 2023-07-15 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_customer_registrationdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_registrationdb',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer_registrationdb',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
