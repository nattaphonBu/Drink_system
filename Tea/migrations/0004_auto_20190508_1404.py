# Generated by Django 2.1.7 on 2019-05-08 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tea', '0003_auto_20190503_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='start_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Start Date'),
        ),
        migrations.AddField(
            model_name='account',
            name='status_account',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Customer', 'Customer'), ('Employee', 'Employee')], default='Customer', max_length=30),
        ),
        migrations.AlterField(
            model_name='tea',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
