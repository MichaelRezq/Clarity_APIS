from rest_framework import serializers
from posts.models import Post
from django.contrib.auth.models import User
from users.api.serializers import UserSerializer


class PostSerializerForGet(serializers.ModelSerializer):
    # image=serializers.ImageField(required=False)
    # video=serializers.FileField(required=False)
    # title=serializers.CharField(required=False)
    # content=serializers.CharField(required=False)
    # Nested serializer for author field
    author = UserSerializer()
    # Nested serializer for likes field
    # likes = UserSerializer(many=True, read_only=True)
    # String representation of tag names
    # tags = serializers.StringRelatedField(many=True)

    
    class Meta:
        model = Post
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    # image=serializers.ImageField(required=False)
    # video=serializers.FileField(required=False)
    # title=serializers.CharField(required=False)
    # content=serializers.CharField(required=False)
    # Nested serializer for author field
    # author = UserSerializer()
    # Nested serializer for likes field
    # likes = UserSerializer(many=True, read_only=True)
    # String representation of tag names
    # tags = serializers.StringRelatedField(many=True)

    
    class Meta:
        model = Post
        fields = '__all__'
