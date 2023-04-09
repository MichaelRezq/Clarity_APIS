# Generated by Django 3.2.12 on 2023-04-05 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20230405_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='position',
            field=models.CharField(choices=[('S', 'Senior'), ('J', 'Junior'), ('I', 'Intermediate'), ('P', 'Professional'), ('f', 'Fresh Graduate')], default='f', max_length=10),
        ),
    ]
