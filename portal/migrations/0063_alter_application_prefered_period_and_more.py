# Generated by Django 4.0.3 on 2022-05-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0062_rename_part_of_profile_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='prefered_period',
            field=models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Online', 'Online')], default=('Full-time', 'Full-time'), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('In progress', 'In progress'), ('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Approved', 'Approved')], default=('In progress', 'In progress'), max_length=50, null=True),
        ),
    ]
