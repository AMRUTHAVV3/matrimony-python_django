# Generated by Django 4.2 on 2023-07-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimonyapp', '0003_customerdb_quali'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdb',
            name='dob',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
