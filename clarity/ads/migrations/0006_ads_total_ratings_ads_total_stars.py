# Generated by Django 4.1.7 on 2023-04-06 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='total_ratings',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ads',
            name='total_stars',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
