# Generated by Django 4.2 on 2023-07-29 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_sendmessagemaledb'),
    ]

    operations = [
        migrations.DeleteModel(
            name='sendmessagemaledb',
        ),
        migrations.AlterField(
            model_name='sendmessagedb',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
