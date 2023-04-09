from rest_framework import serializers
from about.models import About
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

