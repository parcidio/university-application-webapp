# Generated by Django 4.0.3 on 2022-05-23 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0090_alter_application_current_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='current_step',
            field=models.SmallIntegerField(blank=True, default=0, null=True),
        ),
    ]
