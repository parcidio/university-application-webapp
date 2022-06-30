# Generated by Django 4.0.3 on 2022-05-19 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0075_alter_school_leaving_exam_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsor',
            old_name='name',
            new_name='postal_address',
        ),
        migrations.AddField(
            model_name='sponsor',
            name='cellphone',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='sponsor_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='telephone',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='cellphone_number_1',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='cellphone_number_2',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='telephone',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='credits',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='number_years',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='tuition_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='employer',
            name='employer_telephone',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kin',
            name='Work_telephone',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kin',
            name='cellphone_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kin',
            name='telephone',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='permit_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='school_leaving_subject',
            name='point',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='registration_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='student_fund',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='tuition_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='credits',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='level',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]