# Generated by Django 4.0.3 on 2022-05-03 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0012_alter_programme_authority_alter_programme_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='credits',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='years',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]