from requests import Response
from rest_auth.registration.views import RegisterView
from users.models import Custom

from posts.api.views import CustomPagination 
from .serializers import CustomRegisterSerializer, UserSerializer,UserSerializerForGet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BaseAuthentication,TokenAuthentication
from permissions import IsAutherOrReadOnly


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
    search_fields = ['title', 'content']  # Specify the fields to search
    ordering_fields = ['title', 'created_at']  # Specify the fields to order by
    # authentication_classes=[TokenAuthentication]
    # permission_classes = [IsAuthenticated]

# Retrieve, update or delete a post instance
class UsertRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Custom.objects.all()
    serializer_class = UserSerializer
    # authentication_classes=[TokenAuthentication]
    # permission_classes = [IsAuthenticated]

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