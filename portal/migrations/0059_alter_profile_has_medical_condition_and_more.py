# Generated by Django 4.0.3 on 2022-05-16 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0058_alter_profile_has_medical_condition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='has_medical_condition',
            field=models.CharField(choices=[('NO', 'NO'), ('YES', 'YES')], default=('NO', 'NO'), max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='has_medical_needs',
            field=models.CharField(choices=[('NO', 'NO'), ('YES', 'YES')], default=('NO', 'NO'), max_length=20),
        ),
    ]
