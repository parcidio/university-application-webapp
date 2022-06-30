# Generated by Django 4.0.3 on 2022-05-18 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0067_alter_application_prefered_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='prefered_period',
            field=models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Online', 'Online')], default=1, max_length=50),
        ),
    ]
