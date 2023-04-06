from rest_framework import serializers
from events.models import Event,ApplyToEvent
from users.api.serializers import UserSerializer
from django.conf import settings

# class UserForEventsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = settings.AUTH_USER_MODEL
#         fields = ('id','first_name','last_name','phone','facebook_link', 'username', 'email','image','community','country')  # Specify the fields you want to include


class EventSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    applied_by = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Event
        fields = '__all__'

class EventPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['applied_by',]

class ApplyToEventSerializer(serializers.ModelSerializer):
    # author = UserSerializer()
    # applied_by = UserSerializer(many=True, read_only=True)
    class Meta:
        model = ApplyToEvent
        fields = '__all__'