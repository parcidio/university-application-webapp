# Generated by Django 4.0.3 on 2022-05-10 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0037_alter_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_leaving_subject',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.school_leaving'),
        ),
    ]
