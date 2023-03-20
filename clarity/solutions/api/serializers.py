from rest_framework import serializers
from posts.api.serializers import UserSerializer

from problems.api.serializers import ProblemSerializer
from solutions.models import Solution






# Serializer for Solution model
class SolutionSerializer(serializers.ModelSerializer):
    # Nested serializer for problem field
    # problem = ProblemSerializer(read_only=True)
    # Nested serializer for author field
    # author = UserSerializer(read_only=True)
    class Meta:
        model = Solution
        fields = '__all__'
