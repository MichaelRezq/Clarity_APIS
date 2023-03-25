from django.contrib import admin

from .models import Solution,Rating

class SolutionAdmin(admin.ModelAdmin):
    list_display=['id','problem','content']

class RatingAdmin(admin.ModelAdmin):
    list_display=['id','solution','stars','user']

admin.site.register(Solution)
admin.site.register(Rating)