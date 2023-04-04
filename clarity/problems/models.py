from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
# Create your models here.

class Problem(models.Model):
    title = models.CharField(max_length=255) # The title of the problem
    description = models.TextField() # The main content of the problem
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='problems') # The author of the problem
    author_name = models.CharField(max_length=255)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # The date and time the problem was created
    updated_at = models.DateTimeField(auto_now=True) # The date and time the problem was last updated
    image = models.ImageField(upload_to='media/problem_images/', null=True, blank=True) # An optional image for the problem
    tags = ArrayField(models.CharField(max_length=200), blank=True,null=True)
    community = models.CharField(max_length=255)
    views = models.IntegerField(default=0) # The number of views for the problem

    # num_answer = models.IntegerField()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('problem_detail', kwargs={'pk': self.pk}) # Returns the URL to the detail view of the problem

    def get_num_of_answer(self):
        num_answer =  Solution.objects.filter(problem=self).count()
        return num_answer

    @classmethod
    def total_problems(cls,community):
        return cls.objects.filter(community=community).count()

    def increment_views(self, request):
        session_key = 'view_problem_{}'.format(self.pk)
        if not request.session.get(session_key, False):
            self.views += 1
            self.save()
            request.session[session_key] = True

class Solution(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255,null=True,blank=True)
    solution = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)  # The date and time the problem was created
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)  # The date and time the problem was last updated
    community = models.CharField(max_length=255)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes_solution')

    def __str__(self):
        return self.problem.title

    @classmethod
    def total_solution(cls, community):
        return cls.objects.filter(community=community).count()


# class Like(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     solution = models.ForeignKey(Solution, on_delete=models.CASCADE)
#     liked = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)