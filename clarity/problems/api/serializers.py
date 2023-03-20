from rest_framework import serializers
from problems.models import  Problem

from posts.api.serializers import UserSerializer
# Serializer for Problem model
class ProblemSerializer(serializers.ModelSerializer):
    # Nested serializer for author field
    author = UserSerializer(read_only=True)
    class Meta:
        model = Problem
        fields = '__all__'
