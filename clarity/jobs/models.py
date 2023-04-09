
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField





class Job(models.Model):
    """
    Model representing a job listing on LinkedIn.
    """

    # Choices for job types
    FULL_TIME = 'Full_time'
    PART_TIME = 'Part_time'
    CONTRACT = 'Contract'
    INTERNSHIP = 'Internship'
    JOB_TYPE_CHOICES = [
        (FULL_TIME, ('Full-time')),
        (PART_TIME, ('Part-time')),
        (CONTRACT, ('Contract')),
        (INTERNSHIP, ('Internship')),
    ]
    S= "Senior"
    J= 'Junior'
    I='Intermediate'
    P='Professional'
    f='FreshGraduate'

    POSITION_LEVELS = [    (S,'Senior'),    (J , 'Junior'),    (I, 'Intermediate'),    (P, 'Professional'), ( f,'Fresh Graduate')]


    title = models.CharField(('Title'), max_length=255)
    company = models.CharField(('Company'), max_length=255)
    description = models.TextField(('Description'))
    Responsibilities = ArrayField(models.TextField(),null=True)
    Qualification = ArrayField(models.TextField(),null=True)
    skills = ArrayField(models.TextField(),null=True)

    salary=models.DecimalField(max_digits=8, decimal_places=2)
    job_type = models.CharField(('Job type'), max_length=20, choices=JOB_TYPE_CHOICES)
    posted_at = models.DateTimeField(('Posted at'), auto_now_add=True)
    updated_at = models.DateTimeField(('Updated at'), auto_now=True)
    url = models.URLField(('URL'))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='jobs')
    comunity=models.CharField(max_length=50)
    Experience=models.IntegerField(default=0, blank=True, null=True)
    position = models.CharField(max_length=100, choices=POSITION_LEVELS)

    country = models.CharField(('country'), max_length=20, null=True)
    region = models.CharField(('region'), max_length=20, null=True)
    city = models.CharField(('city'), max_length=20, null=True)
    postcode = models.IntegerField(('postcode'), max_length=10, null=True)
    full_address = models.TextField(('full_address'), max_length=255, null=True)



    def __str__(self):
        return self.title


    class Meta:
        verbose_name = ('Job')
        verbose_name_plural = ('Jobs')
        ordering = ['-posted_at']