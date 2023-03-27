# Generated by Django 4.1.7 on 2023-03-27 15:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='custom',
            name='date_birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='custom',
            name='facebook_link',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='custom',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='custom',
            name='phone',
            field=models.CharField(max_length=14, null=True, validators=[django.core.validators.RegexValidator(message='phone must be an egyptian phone number...', regex='^01[1|0|2|5][0-9]{8}$')], verbose_name='phone'),
        ),
        migrations.AddField(
            model_name='custom',
            name='photo',
            field=models.ImageField(default='test', upload_to='users/images', verbose_name='photo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='custom',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='custom',
            name='username',
            field=models.CharField(default='username', max_length=50, verbose_name='user_name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='custom',
            name='email',
            field=models.EmailField(max_length=150, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='custom',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='custom',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='custom',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='last_name'),
        ),
    ]
