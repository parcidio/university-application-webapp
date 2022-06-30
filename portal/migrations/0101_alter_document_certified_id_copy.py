# Generated by Django 4.0.3 on 2022-05-30 21:34

from django.db import migrations, models
import portal.models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0100_alter_document_certified_id_copy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='certified_id_copy',
            field=models.FileField(blank=True, null=True, upload_to=portal.models.user_directory_path),
        ),
    ]