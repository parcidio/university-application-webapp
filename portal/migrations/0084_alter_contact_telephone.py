# Generated by Django 4.0.3 on 2022-05-23 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0083_alter_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='telephone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
