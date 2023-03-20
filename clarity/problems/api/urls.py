from django.urls import path
from .views import ProblemListCreateView, ProblemRetrieveUpdateDeleteView

urlpatterns = [
    path('problems/', ProblemListCreateView.as_view(), name='problem_list_create'),
    path('problems/<int:pk>/', ProblemRetrieveUpdateDeleteView.as_view(), name='problem_retrieve_update_delete'),
]
