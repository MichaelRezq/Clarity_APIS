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