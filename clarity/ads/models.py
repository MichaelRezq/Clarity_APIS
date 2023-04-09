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
    # new fields for rate and review
    total_ratings = models.PositiveIntegerField(default=0)
    total_stars = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def get_average_rating(self):
        ratings = self.reviews.all()
        if ratings.count() == 0:
            return 0
        else:
            total_rating = sum([rating.rating for rating in ratings])
            return total_rating / ratings.count()

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )
    ad = models.ForeignKey(Ads, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.ad} - {self.user}'


