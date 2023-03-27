from django.contrib.auth import get_user_model
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from community.models import Community

class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    community = serializers.PrimaryKeyRelatedField(queryset=Community.objects.all(), many=False)
    photo=serializers.ImageField(required=True)
    country=serializers.CharField(required=True)
    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.community = self.validated_data.get('community', '')
        user.photo = self.validated_data.get('photo', '')
        user.country = self.validated_data.get('country', '')
        user.save(update_fields=['first_name', 'last_name', 'community'])

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['first_name'] = self.validated_data.get('first_name', '')
        data_dict['last_name'] = self.validated_data.get('last_name', '')
        data_dict['community'] = self.validated_data.get('community', '')
        data_dict['photo'] = self.validated_data.get('photo', '')
        data_dict['country'] = self.validated_data.get('country', '')
        return data_dict
