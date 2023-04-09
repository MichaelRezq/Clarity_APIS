from django.urls import path
from .views import get_post_ads ,get_edit_delete_ads,add_review,update_review
urlpatterns = [
    path('ads/', get_post_ads, name='ads_list_create'),
    path('ads/<int:pk>/', get_edit_delete_ads, name='ads_retrieve_update_delete'),
    path('ads/<int:pk>/review/', add_review, name='create_review'),
    path('ads/<int:pk>/review/<int:review_pk>/', update_review, name='update_review'),
]
