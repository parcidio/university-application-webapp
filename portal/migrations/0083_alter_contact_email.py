# Generated by Django 4.0.3 on 2022-05-23 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0082_termsandconditions_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]