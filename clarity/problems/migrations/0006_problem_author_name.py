# Generated by Django 4.1.7 on 2023-03-28 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0005_solution_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='author_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
