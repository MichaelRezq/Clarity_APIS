from django.urls import path
from .views import get_post_problems , get_spesific_post , get_post_comment , get_edit_delete_comment , LikeView,ShareView

urlpatterns = [
    path('posts/', get_post_problems, name='posts'),
    path('posts/<int:pk>/', get_spesific_post , name='post_detail'),
    path('post/<int:postid>/comments', get_post_comment, name='comments'),
    path('comment/<int:postid>/<int:commentid>', get_edit_delete_comment, name='comments_retrieve_update_delete'),
    path('posts/<int:post_id>/like', LikeView.as_view(), name='like_view'),
    path('posts/<int:post_id>/share', ShareView.as_view(), name='share_view'),
]
