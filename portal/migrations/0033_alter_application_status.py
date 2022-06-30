# Generated by Django 4.0.3 on 2022-05-05 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0032_alter_application_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('inprogress', 'In progress'), ('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Approved', 'Approved')], default=('inprogress', 'In progress'), max_length=50),
        ),
    ]
