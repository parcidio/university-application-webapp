# Generated by Django 4.0.3 on 2022-05-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_alter_programme_authority_alter_programme_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programme',
            name='authority',
            field=models.CharField(choices=[('NQA', 'Namibia Qualification Authority')], max_length=50),
        ),
    ]
