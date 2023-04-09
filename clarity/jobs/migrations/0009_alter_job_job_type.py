# Generated by Django 3.2.12 on 2023-04-07 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_remove_job_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full_time', 'Full-time'), ('Part_time', 'Part-time'), ('Contract', 'Contract'), ('Internship', 'Internship')], max_length=20, verbose_name='Job type'),
        ),
    ]