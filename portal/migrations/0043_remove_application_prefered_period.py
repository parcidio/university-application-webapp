# Generated by Django 4.0.3 on 2022-05-11 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0042_application_prefered_campus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='prefered_period',
        ),
    ]
