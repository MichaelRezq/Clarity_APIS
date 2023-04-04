from rest_framework import serializers
from ads.models import  Ads
    # ,Like

from posts.api.serializers import UserSerializer
# Serializer for Problem model
class AdsSerializer(serializers.ModelSerializer):
    # Nested serializer for author field
    # author = UserSerializer(read_only=True)
    # get_num_of_answer = serializers.SerializerMethodField()
    # total_problems = serializers.SerializerMethodField()

    class Meta:
        model = Ads
        fields = ('__all__')

