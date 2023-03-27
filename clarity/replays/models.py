from django.conf import settings
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
from comments.models import Comment

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_replies') # The comment the reply is associated with
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='auther_replies') # The author of the reply
    content = models.TextField() # The main content of the reply
    created_at = models.DateTimeField(auto_now_add=True) # The date and time the reply was created
    updated_at = models.DateTimeField(auto_now=True) # The date and time the reply was last updated

    def __str__(self):
        return self.content
