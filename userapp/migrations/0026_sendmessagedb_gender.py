# Generated by Django 4.2 on 2023-08-03 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0025_alter_receivemsgdb_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendmessagedb',
            name='gender',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]