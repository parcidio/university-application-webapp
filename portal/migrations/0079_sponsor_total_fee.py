# Generated by Django 4.0.3 on 2022-05-19 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0078_sponsor_sponsorship_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='total_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
