# Generated by Django 4.2 on 2023-08-03 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0023_remove_receivemsgdb_user_receivemsgdb_user_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receivemsgdb',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='receivemsgdb',
            name='message',
        ),
    ]
