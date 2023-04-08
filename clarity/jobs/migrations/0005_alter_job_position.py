# Generated by Django 3.2.12 on 2023-04-05 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_job_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='position',
            field=models.CharField(choices=[('Senior', 'Senior'), ('Junior', 'Junior'), ('Intermediate', 'Intermediate'), ('Professional', 'Professional'), ('Fresh Graduate', 'Fresh Graduate')], default='f', max_length=100),
        ),
    ]
