# Generated by Django 4.0.3 on 2022-06-07 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0102_application_programme'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='other_level',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
