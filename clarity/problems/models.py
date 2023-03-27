from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Problem(models.Model):
    title = models.CharField(max_length=255) # The title of the problem
    content = models.TextField() # The main content of the problem
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='problems') # The author of the problem
    created_at = models.DateTimeField(auto_now_add=True) # The date and time the problem was created
    updated_at = models.DateTimeField(auto_now=True) # The date and time the problem was last updated
    image = models.ImageField(upload_to='media/problem_images/', null=True, blank=True) # An optional image for the problem

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('problem_detail', kwargs={'pk': self.pk}) # Returns the URL to the detail view of the problem
