# Generated by Django 4.1.7 on 2023-04-08 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('organization', models.CharField(choices=[('iti', 'ITI'), ('mahara-tech', 'MAHARA-TECH'), ('udemy', 'UDEMY'), ('coursera', 'COURSERA'), ('udacity', 'UDACITY'), ('online', 'ONLINE'), ('other', 'OTHER')], default='ITI', max_length=20)),
                ('certificaty_URL', models.CharField(blank=True, max_length=300, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
