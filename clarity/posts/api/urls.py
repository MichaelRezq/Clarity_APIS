from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateDeleteView

urlpatterns = [
    path('posts', PostListCreateView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostRetrieveUpdateDeleteView.as_view(), name='post_detail'),
]
