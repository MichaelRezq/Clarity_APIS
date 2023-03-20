from rest_framework import generics, filters,permissions
from rest_framework.pagination import PageNumberPagination

from posts.api.views import CustomPagination

from problems.models import  Problem
from .serializers import  ProblemSerializer



# ------------------- PROBLEMS -------------------

# List all problems or create a new problem
class ProblemListCreateView(generics.ListCreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    pagination_class = CustomPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']  # Specify the fields to search

# Retrieve, update or delete a problem instance
class ProblemRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]






