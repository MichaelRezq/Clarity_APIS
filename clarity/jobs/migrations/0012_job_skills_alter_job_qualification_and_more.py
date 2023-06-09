# Generated by Django 4.1.7 on 2023-04-08 03:38

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_alter_job_position_alter_job_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='skills',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='job',
            name='Qualification',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='job',
            name='Responsibilities',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None),
        ),
    ]
