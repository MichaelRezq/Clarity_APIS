from rest_framework import serializers
from problems.models import  Problem,Solution\
    # ,Like

from posts.api.serializers import UserSerializer
# Serializer for Problem model
class ProblemSerializer(serializers.ModelSerializer):
    # Nested serializer for author field
    # author = UserSerializer(read_only=True)
    get_num_of_answer = serializers.SerializerMethodField()
    # total_problems = serializers.SerializerMethodField()

    class Meta:
        model = Problem
        fields = ('id','title','description','author','author_name','created_at','tags','community','get_num_of_answer')

    def get_num_of_answer(self,obj):
        return obj.get_num_of_answer

    # def total_problems(self,obj):
    #     return obj.total_problems

class SolutionSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Solution
        fields = ('id','user','problem','user_name','solution','created_at','community','likes')

    def get_likes(self, obj):
        return obj.likes.count()


# class LikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Like
#         fields = '__all__'
