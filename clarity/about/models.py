from django.db import models
from django.conf import settings

# Create your models here.
ORGANIZATION_CHOICES = (
    ('iti','ITI'),
    ('mahara-tech', 'MAHARA-TECH'),
    ('udemy','UDEMY'),
    ('coursera','COURSERA'),
    ('udacity','UDACITY'),
    ('online','ONLINE'),
    ('other','OTHER'),

)


class About(models.Model):
        skill_name = models.CharField(max_length=255)
        author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , null=True , blank=True) # The author of the post
        description=models.TextField(null=True , blank=True)
        organization = models.CharField(max_length=20, choices=ORGANIZATION_CHOICES, default='ITI')
        certificaty_URL=models.CharField(max_length=300 , null=True , blank=True)

        # def __str__(self):
        #  return self.skill_name
    
