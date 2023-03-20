from django.urls import path
from .views import CommentReplyList, CommentReplyDetail

urlpatterns = [
    path('comment-replies/', CommentReplyList.as_view(), name='comment_reply_list'),
    path('comment-replies/<int:pk>/', CommentReplyDetail.as_view(), name='comment_reply_detail'),
]
