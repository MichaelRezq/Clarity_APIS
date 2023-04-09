from rest_framework import serializers
from ads.models import  Ads,Review
    # ,Like

# from posts.api.serializers import UserSerializer
# Serializer for Problem model
from users.models import Custom

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom
        fields = '__all__'

class ReviewSerializerGet(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'ad', 'user', 'rating', 'comment', 'created_at')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'ad', 'user', 'rating', 'comment', 'created_at')

class AdsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializerGet(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    def get_average_rating(self, obj):
        return obj.get_average_rating()

    class Meta:
        model = Ads
        fields = ('id', 'name', 'description', 'author', 'created_at', 'updated_at', 'image', 'type', 'siteUrl', 'country', 'region', 'street', 'services', 'total_ratings', 'total_stars', 'reviews','average_rating')




# class AdsSerializer(serializers.ModelSerializer):
#     # Nested serializer for author field
#     # author = UserSerializer(read_only=True)
#     # get_num_of_answer = serializers.SerializerMethodField()
#     # total_problems = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Ads
#         fields = ('__all__')

