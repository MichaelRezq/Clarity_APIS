from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BaseAuthentication,TokenAuthentication
from permissions import IsAutherOrReadOnly
from posts.models import Post
from .serializers import PostSerializer


# Set the pagination parameters
class CustomPagination(PageNumberPagination):
    page_size = 10  # Number of results per page
    page_size_query_param = 'page_size'  # Query parameter to override `page_size`
    max_page_size = 100  # Maximum number of results per page


# ------------------- POSTS -------------------

# List all posts or create a new post
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']  # Specify the fields to search
    ordering_fields = ['title', 'created_at']  # Specify the fields to order by
    # authentication_classes=[TokenAuthentication]
    # permission_classes = [IsAuthenticated]

# Retrieve, update or delete a post instance
class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAutherOrReadOnly]
