# Generated by Django 4.0.3 on 2022-05-04 21:55

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0022_course_course_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='status',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Approved', 'Approved')], max_length=25, null=True),
        ),
    ]
