from rest_framework import serializers
from posts.models import Post
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):
    # Nested serializer for author field
    author = UserSerializer(read_only=True)
    # Nested serializer for likes field
    likes = UserSerializer(many=True, read_only=True)
    # String representation of tag names
    # tags = serializers.StringRelatedField(many=True)
    class Meta:
        model = Post
        fields = '__all__'

# # Serializer for Tag model
# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = 'all'
# # Serializer for PostTag model
# class PostTagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostTag
#         fields = 'all'