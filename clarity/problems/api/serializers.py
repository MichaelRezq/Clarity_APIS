from rest_framework import serializers
from problems.models import  Problem,Solution\
    # ,Like

from users.api.serializers import UserSerializer
# Serializer for Problem model
from users.models import Custom

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom
        fields = '__all__'

class ProblemSerializer(serializers.ModelSerializer):
    # Nested serializer for author field
    # author = UserSerializer(read_only=True)
    get_num_of_answer = serializers.SerializerMethodField()
    # total_problems = serializers.SerializerMethodField()

    class Meta:
        model = Problem
        fields = ('id','title','description','author','author_name','created_at','tags','community','get_num_of_answer','views','body')

    def get_num_of_answer(self,obj):
        return obj.get_num_of_answer

class ProblemSerializerGet(serializers.ModelSerializer):
    # Nested serializer for author field
    author = UserSerializer(read_only=True)
    get_num_of_answer = serializers.SerializerMethodField()

    # total_problems = serializers.SerializerMethodField()

    class Meta:
        model = Problem
        fields = ('id', 'title', 'description', 'author', 'author_name', 'created_at', 'tags', 'community',
                  'get_num_of_answer', 'views', 'body')

    def get_num_of_answer(self, obj):
        return obj.get_num_of_answer

# def total_problems(self,obj):
#     return obj.total_problems

class SolutionSerializerGet(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Solution
        fields = ('id','user','problem','user_name','solution','created_at','community','likes','user')

    # def get_likes(self, obj):
    #     return obj.likes.count()

    def get_likes(self, obj):
        likes = obj.likes.all()
        num_likes = obj.likes.count()
        return [{
            'solution_id': obj.id,
            'user': like.username,
            'user_id': like.id,
            'num_likes': num_likes
        } for like in likes]

class SolutionSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Solution
        fields = ('id','user','problem','user_name','solution','created_at','community','likes')

    # def get_likes(self, obj):
    #     return obj.likes.count()

    def get_likes(self, obj):
        likes = obj.likes.all()
        num_likes = obj.likes.count()
        return [{
            'solution_id': obj.id,
            'user': like.username,
            'user_id': like.id,
            'num_likes': num_likes
        } for like in likes]



# class LikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Like
#         fields = '__all__'
