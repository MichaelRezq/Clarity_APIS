from rest_framework import serializers
from posts.models import Post
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):
    # Nested serializer for author field
    # author = UserSerializer(read_only=True)
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



# A serializer is a class in Django REST framework that converts complex data types, 
# such as Django model instances, 
# into Python data types that can be easily rendered into JSON, XML or other content types.
#  It essentially provides a way to convert the data from one format to another,
#  making it easy to transmit data over the internet in a structured and organized way. 
# Serializers also handle validating incoming data and deserializing incoming data into complex types,
#  such as Django model instances.