# Generated by Django 4.0.3 on 2022-05-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0092_acknowledgement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acknowledgement',
            name='application_form_acknowledgement',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
