# Generated by Django 4.1.7 on 2023-04-03 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0010_alter_solution_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]