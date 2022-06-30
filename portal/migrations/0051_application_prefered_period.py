# Generated by Django 4.0.3 on 2022-05-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0050_remove_application_prefered_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='prefered_period',
            field=models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Online', 'Online')], default=('Full-time', 'Full-time'), max_length=50),
        ),
    ]
