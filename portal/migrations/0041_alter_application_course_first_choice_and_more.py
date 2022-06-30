# Generated by Django 4.0.3 on 2022-05-11 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0040_alter_profile_date_of_birth_alter_profile_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='course_first_choice',
            field=models.ForeignKey(blank=True, default='choose your first choice', null=True, on_delete=models.SET('deleted'), to='portal.course'),
        ),
        migrations.AlterField(
            model_name='application',
            name='course_second_choice',
            field=models.ForeignKey(blank=True, default='choose your second choice', null=True, on_delete=models.SET('deleted'), to='portal.secondary_course'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='has_medical_condition',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO'), ('MAYBE', 'MAYBE')], default=('NO', 'NO'), max_length=20, null=True),
        ),
    ]
