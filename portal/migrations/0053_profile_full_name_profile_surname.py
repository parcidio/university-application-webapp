# Generated by Django 4.0.3 on 2022-05-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0052_profile_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='surname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
