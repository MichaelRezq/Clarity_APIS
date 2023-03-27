from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse

from posts.models import Post

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') # The post that the comment belongs to
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments') # The user who wrote the comment
    content = models.TextField() # The content of the comment
    created_at = models.DateTimeField(auto_now_add=True) # The date and time the comment was created
    updated_at = models.DateTimeField(auto_now=True) # The date and time the comment was last updated
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies') # A foreign key to another comment, if this comment is a reply

    def __str__(self):
        return self.content