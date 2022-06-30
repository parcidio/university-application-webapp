# Generated by Django 4.0.3 on 2022-05-03 07:44

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_alter_subject_faculty_alter_subject_lecturer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campus',
            name='location',
        ),
        migrations.AddField(
            model_name='campus',
            name='Town',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='campus',
            name='address',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='campus',
            name='country',
            field=django_countries.fields.CountryField(default='Namibia', max_length=2),
        ),
    ]
