# Generated by Django 4.2 on 2023-07-29 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_delete_sendmessagemaledb_alter_sendmessagedb_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendmessagedb',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
