from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


from problems.models import Problem
# Create your models here.


class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='solutions') # The problem that the solution belongs to
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solutions') # The user who wrote the solution
    content = models.TextField() # The content of the solution
    created_at = models.DateTimeField(auto_now_add=True) # The date and time the solution was created
    updated_at = models.DateTimeField(auto_now=True) # The date and time the solution was last updated
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies') # A foreign key to another solution, if this solution is a reply
    is_accepted = models.BooleanField(default=False) # A boolean field indicating whether this solution has been accepted as
