from django.http import JsonResponse
from requests import Response
from rest_auth.registration.views import RegisterView
from users.models import Custom

from posts.api.views import CustomPagination 
from .serializers import CustomRegisterSerializer, UserSerializer,UserSerializerForGet,UserSerializerFOrPut
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics, filters,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
    parser_classes = (MultiPartParser, FormParser)


# ------------------- custom user -------------------

# List all users
class UserListCreateView(generics.ListCreateAPIView):
    queryset = Custom.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'username','last_name']  # Specify the fields to search
    ordering_fields = [ 'first_name']  # Specify the fields to order by

# Retrieve, update or delete a post instance
class UsertRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Custom.objects.all()
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        self.serializer_class = UserSerializerFOrPut
        user = self.get_object() # Get the Event object to modify
        print("-------------------------event----------------",user)
        user_id = request.user.id# Get the user id to remove
        print('----------------------user id ---------------------',user_id)
         #Update the user object with the data provided in the request
        serializer = self.serializer_class(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': 'the user updated the profile successfully'},status=status.HTTP_200_OK)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed

class UserDetailView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer()

    def get(self, request):
        try:
            user = TokenAuthentication().authenticate(request)
            # user is a tuple of (user, token)
            # you can access the user with user[0]
            UserModel = Custom
            user_obj = UserModel.objects.get(id=user[0].id)
            # user_obj is the authenticated user object
            serializer = UserSerializerForGet(user_obj)
            return Response(serializer.data)
        except AuthenticationFailed:
            return Response({'error': 'Invalid token'})
        

from django.shortcuts import redirect

def verified_email_redirect(request):
    # redirect to the desired URL after successful email verification
    return redirect('/my/custom/http://localhost:3000/')



from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# @csrf_exempt
# @api_view(['GET', 'POST'])
# def change_password(request):
#     if request.method == 'POST':
#         print(request.POST)
#         current_password = request.POST.get('current_password')
#         new_password = request.POST.get('new_password')
#         confirm_password = request.POST.get('confirm_password')
#         user = TokenAuthentication().authenticate(request)
#         UserModel = Custom
#         user_obj = UserModel.objects.get(id=user[0].id)
#         # user_obj is the authenticated user object
#         serializer = UserSerializerForGet(user_obj)
#         print(serializer.data)
#         print(user[1])
#         # user = authenticate(username=request.user.username, password=current_password)
#         print('=======================',current_password)
#         if user is None:
#             return JsonResponse({'error': 'Current password is incorrect.'}, status=400)
#         if new_password != confirm_password:
#             return JsonResponse({'error': 'New password and confirmation do not match.'}, status=400)
#         # user.set_password(new_password)
#         # user.save()
#         return JsonResponse({'message': 'Password updated successfully.'}, status=200)


#---------------------------- friends--------------------------------
# send friend request
from django.contrib.auth.models import User
from rest_framework import generics, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import FriendRequest
from .serializers import FriendRequestSerializer

class FriendRequestListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        return FriendRequest.objects.filter(sender=self.request.user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class FriendRequestDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

class FriendRequestPendingAPIView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        return FriendRequest.objects.filter(recipient=self.request.user, status='pending')

class FriendRequestAcceptAPIView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        friend_request = self.get_object()
        friend_request.status = 'accepted'
        friend_request.save()
        serializer = self.get_serializer(friend_request)
        return Response(serializer.data)

class FriendRequestDeclineAPIView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        friend_request = self.get_object()
        friend_request.status = 'declined'
        friend_request.save()
        serializer = self.get_serializer(friend_request)
        return Response(serializer.data)



from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate

@api_view(['POST'])
def change_password(request):
    print(request)

    user = request.user
    old_password = request.data.get('old_password')
    print('old_password',old_password)
    new_password = request.data.get('new_password')
    print('new_password',new_password)

    # if not authenticate(id=user.id, password=old_password):
    #     print('old password---------------------',user.password)
    #     return Response({'error': 'Incorrect old password.'}, status=400)
    user.set_password(new_password)
    user.save()

    return Response({'success': 'Password updated successfully.'}, status=200)
