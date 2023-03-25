from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

from problems.models import Problem
# Create your models here.


class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='problem_solutions') # The problem that the solution belongs to
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auther_solutions') # The user who wrote the solution
    content = models.TextField() # The content of the solution
    created_at = models.DateTimeField(auto_now_add=True) # The date and time the solution was created
    updated_at = models.DateTimeField(auto_now=True) # The date and time the solution was last updated
    # parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies') # A foreign key to another solution, if this solution is a reply
    is_accepted = models.BooleanField(default=False) # A boolean field indicating whether this solution has been accepted as


    def __str__(self):
        return self.content
    

    def no_of_rating(self):
        ratings= Solution.objects.filter(solution=self)
        return len(ratings)

   
    def avg_rating(self):
        sum=0
        ratings= Solution.objects.filter(solution=self)
        # sum of each rate / sum of number of ratings
        for rat in ratings:
            sum += rat.stars
        if len(ratings) > 0 :
            return sum / len(ratings)
        else:
            return 0
class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    solution=models.ForeignKey(Solution,on_delete=models.CASCADE)
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    
    class Meta:
        unique_together = (('user', 'stars'),)
        index_together=(('user','stars'),)
    