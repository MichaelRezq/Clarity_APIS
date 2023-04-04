from django.contrib import admin
from .models import Problem,Solution

# Register your models here.

class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at', 'author')

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Solution)
