# Generated by Django 4.2 on 2023-07-21 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_rename_place_customer_registrationdb_occupation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='sendmessagedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]