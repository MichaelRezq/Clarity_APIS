# Generated by Django 4.1.7 on 2023-04-09 04:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_author_comment_parent_comment_post'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('replays', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='auther_replies', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reply',
            name='comment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comment_replies', to='comments.comment'),
            preserve_default=False,
        ),
    ]
