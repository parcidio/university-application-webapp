# Generated by Django 4.0.3 on 2022-05-10 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0036_alter_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('In progress', 'In progress'), ('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Approved', 'Approved')], default=('In progress', 'In progress'), max_length=50),
        ),
    ]