# Generated by Django 4.2 on 2023-07-29 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0011_alter_sendmessagedb_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendmessagedb',
            name='user_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
