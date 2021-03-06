# Generated by Django 4.0.3 on 2022-05-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0033_alter_application_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='submition_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('In progress', 'In progress'), ('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Approved', 'Approved')], default=('In progress', 'In progress'), max_length=50),
        ),
    ]
