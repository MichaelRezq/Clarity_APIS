from rest_framework import generics, filters
from posts.api.views import CustomPagination
from solutions.models import   Solution
from .serializers import  SolutionSerializer

# ------------------- SOLUTIONS -------------------

# List all solutions or create a new solution
class SolutionListCreateView(generics.ListCreateAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['content']  # Specify the fields to search

# Retrieve, update or delete a solution instance
class SolutionRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer


