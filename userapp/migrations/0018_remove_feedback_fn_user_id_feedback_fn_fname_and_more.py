# Generated by Django 4.2 on 2023-08-02 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0017_feedback_fn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback_fn',
            name='user_id',
        ),
        migrations.AddField(
            model_name='feedback_fn',
            name='fname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='feedback_fn',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sendmessagedb',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
