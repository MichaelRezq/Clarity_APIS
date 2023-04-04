# Generated by Django 4.1.7 on 2023-03-27 22:46

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_alter_problem_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='community',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='problem',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.TextField()),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.problem')),
            ],
        ),
    ]
