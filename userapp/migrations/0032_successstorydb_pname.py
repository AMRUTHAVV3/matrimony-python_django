# Generated by Django 4.2 on 2023-08-10 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0031_alter_successstorydb_c_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='successstorydb',
            name='pname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
