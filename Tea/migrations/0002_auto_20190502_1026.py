# Generated by Django 2.1.7 on 2019-05-02 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tea', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeofitem',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='typeofitem',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
