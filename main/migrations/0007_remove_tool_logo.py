# Generated by Django 2.1.4 on 2018-12-16 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20181215_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='logo',
        ),
    ]
