from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django .conf import settings
from rest_framework.authtoken.models import Token

class Post(models.Model):
    title = models.CharField(max_length=255) # The title of the post
    content = models.TextField() # The main content of the post
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts') # The author of the post
    created_at = models.DateTimeField(auto_now_add=True) # The date and time the post was created
    updated_at = models.DateTimeField(auto_now=True) # The date and time the post was last updated
    image = models.ImageField(upload_to='media/post_images/', null=True, blank=True) # An optional image for the post
    video = models.FileField(upload_to='media/post_videos/', null=True, blank=True) # An optional video for the post
    likes = models.ManyToManyField(User, related_name='liked_posts', null=True, blank=True) # A ManyToMany field that tracks which users have liked the post
    shared_by = models.ManyToManyField(User, related_name='shared_posts', null=True, blank=True) # A ManyToMany field that tracks which users have shared the post

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk}) # Returns the URL to the detail view of the post





@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)