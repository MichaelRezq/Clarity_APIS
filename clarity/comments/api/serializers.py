from rest_framework import serializers
from django.contrib.auth.models import User
from comments.models import Post, Comment
from posts.api.serializers import UserSerializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']




# Serializer for Comment model
class CommentSerializer(serializers.ModelSerializer):
    # Nested serializer for author field
    author = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
