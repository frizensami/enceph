# Generated by Django 2.1.4 on 2018-12-15 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181215_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='is_beta',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tool',
            name='is_for_developers',
            field=models.BooleanField(default=False),
        ),
    ]
