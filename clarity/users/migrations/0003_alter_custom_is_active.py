# Generated by Django 4.1.7 on 2023-03-27 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_custom_country_custom_date_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]