# Generated by Django 4.1.7 on 2023-03-20 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0002_alter_solution_author_alter_solution_problem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solution',
            name='parent',
        ),
    ]