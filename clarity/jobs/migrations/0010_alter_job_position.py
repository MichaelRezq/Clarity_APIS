# Generated by Django 4.1.7 on 2023-04-08 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_alter_job_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='position',
            field=models.CharField(choices=[('Senior', 'Senior'), ('Ju nior', 'Junior'), ('Int e rmediate', 'Intermediate'), ('Pro f essional', 'Professional'), ('Fre s h Graduate', 'Fresh Graduate')], max_length=100),
        ),
    ]
