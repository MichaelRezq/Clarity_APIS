from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
# Create your models here.

class Ads(models.Model):
    TYPE_CHOICES = (
        ('CO', 'Company'),
        ('RE', 'Restaurant'),
        ('CF', 'Coffe'),
        ('HO', 'Hotel'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ads')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='ads_images', null=True, blank=True)
    type = models.CharField(max_length=3,choices=TYPE_CHOICES)
    siteUrl = models.URLField(max_length = 255)
    country = models.CharField(max_length = 255)
    region = models.CharField(max_length = 255)
    street = models.CharField(max_length = 255)
    services = ArrayField(models.TextField())


    def __str__(self):
        return self.name