# Generated by Django 4.2 on 2023-07-25 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_sendmessagedb_fname_sendmessagedb_lname'),
    ]

    operations = [
        migrations.CreateModel(
            name='sendmessagemaledb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=50, null=True)),
                ('lname', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]