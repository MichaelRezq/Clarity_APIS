from django.urls import path
from .views import SolutionListCreateView, SolutionRetrieveUpdateDeleteView

urlpatterns = [
    path('solutions/', SolutionListCreateView.as_view(), name='solution_list'),
    path('solutions/<int:pk>/', SolutionRetrieveUpdateDeleteView.as_view(), name='solution_detail'),
]
