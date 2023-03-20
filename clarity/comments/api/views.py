from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination

from comments.models import Post, Comment
from .serializers import CommentSerializer
from posts.api.views import CustomPagination


# ------------------- COMMENTS -------------------

# List all comments or create a new comment
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['content']  # Specify the fields to search

# Retrieve, update or delete a comment instance
class CommentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


