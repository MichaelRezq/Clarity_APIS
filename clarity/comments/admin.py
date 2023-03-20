from django.contrib import admin
from .models import Comment
# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'created_at', 'updated_at')
    list_filter = ('author', 'created_at')
    search_fields = ('content',)