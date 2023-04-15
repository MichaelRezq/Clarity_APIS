from django.contrib.auth import get_user_model
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.db import transaction
from django.conf import settings
from chat.models import ChatRoom
from community.api.serializers import CommunitySerializer
from community.models import Community

class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    # community = serializers.CharField(required=True)
    community = serializers.PrimaryKeyRelatedField(queryset=Community.objects.all(), many=False)
    photo=serializers.ImageField(required=False)
    country=serializers.CharField(required=True)
    phone=serializers.CharField(required=True)
    @transaction.atomic
    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.community = self.validated_data.get('community', '')
        user.photo = self.validated_data.get('photo', '')
        user.country = self.validated_data.get('country', '')
        user.phone = self.validated_data.get('phone', '')
        user.save(update_fields=['first_name', 'last_name', 'community','photo','country','phone'])
        chatRoom = ChatRoom.objects.create(type="SELF", name=user.first_name + user.last_name)
		# chatRoom.member.add(user.id)
        print('----------------------------------',request.data)
        print('---------------chatRoom-------------------',chatRoom)


    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['first_name'] = self.validated_data.get('first_name', '')
        data_dict['last_name'] = self.validated_data.get('last_name', '')
        data_dict['community'] = self.validated_data.get('community', '')
        data_dict['photo'] = self.validated_data.get('photo', '')
        data_dict['country'] = self.validated_data.get('country', '')
        data_dict['phone'] = self.validated_data.get('phone', '')
        
        return data_dict


from users.models import Custom

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Custom
        fields = '__all__'
class UserSerializerFOrPut(serializers.ModelSerializer):
    
    class Meta:
        model = Custom
        fields = ['username','first_name','last_name','phone','facebook_link','country','photo','date_birth','cover_photo','job_title','bio']


class UserSerializerForGet(serializers.ModelSerializer):
    community=CommunitySerializer()
    class Meta:
        model = Custom
        fields = '__all__'

from rest_framework import serializers
from users.models import FriendRequest

class FriendRequestSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')
    recipient = serializers.ReadOnlyField(source='recipient.username')

    class Meta:
        model = FriendRequest
        fields = ('id', 'sender', 'recipient', 'timestamp', 'status')
