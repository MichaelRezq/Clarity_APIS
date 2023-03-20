from django.urls import path
from .views import CommentListCreateView, CommentRetrieveUpdateDeleteView

urlpatterns = [
    path('comments/', CommentListCreateView.as_view(), name='comment_list_create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDeleteView.as_view(), name='comment_retrieve_update_delete'),
]
