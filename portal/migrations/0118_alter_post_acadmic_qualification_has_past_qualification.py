# Generated by Django 4.0.3 on 2022-06-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0117_alter_post_acadmic_qualification_has_past_qualification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_acadmic_qualification',
            name='has_past_qualification',
            field=models.CharField(choices=[('NO', 'NO'), ('YES', 'YES')], default='NO', max_length=20, null=True),
        ),
    ]
