# Generated by Django 4.0.3 on 2022-05-19 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0077_sponsor_sponsor_signatory_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='sponsorship_type',
            field=models.CharField(choices=[('Self Sponsored', 'Self Sponsored'), ('Sponsored by a Third-party', 'Sponsored by a Third-party')], default='Self Sponsored', max_length=50),
        ),
    ]
