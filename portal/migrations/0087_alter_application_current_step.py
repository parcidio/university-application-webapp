# Generated by Django 4.0.3 on 2022-05-23 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0086_alter_application_current_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='current_step',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
