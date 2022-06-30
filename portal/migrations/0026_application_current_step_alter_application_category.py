# Generated by Django 4.0.3 on 2022-05-04 22:43

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0025_application_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='current_step',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Shortcourse', 'Shortcourse'), ('Undergraduate', 'Undergraduate'), ('Postgraduate', 'Postgraduate')], max_length=50, null=True),
        ),
    ]
