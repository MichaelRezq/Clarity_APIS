

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse





class Job(models.Model):
    """
    Model representing a job listing on LinkedIn.
    """

    # Choices for job types
    FULL_TIME = 'full_time'
    PART_TIME = 'part_time'
    CONTRACT = 'contract'
    INTERNSHIP = 'internship'
    JOB_TYPE_CHOICES = [
        (FULL_TIME, ('Full-time')),
        (PART_TIME, ('Part-time')),
        (CONTRACT, ('Contract')),
        (INTERNSHIP, ('Internship')),
    ]

    title = models.CharField(('Title'), max_length=255)
    company = models.CharField(('Company'), max_length=255)
    description = models.TextField(('Description'))
    job_type = models.CharField(('Job type'), max_length=20, choices=JOB_TYPE_CHOICES)
    location = models.CharField(('Location'), max_length=255)
    posted_at = models.DateTimeField(('Posted at'), auto_now_add=True)
    updated_at = models.DateTimeField(('Updated at'), auto_now=True)
    url = models.URLField(('URL'), unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='jobs')
    comunity=models.CharField(max_length=50)
    class Meta:
        verbose_name = ('Job')
        verbose_name_plural = ('Jobs')
        ordering = ['-posted_at']