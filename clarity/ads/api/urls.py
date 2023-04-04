from django.urls import path
from .views import get_post_ads ,get_edit_delete_ads
urlpatterns = [
    path('ads/', get_post_ads, name='ads_list_create'),
    path('ads/<int:pk>/', get_edit_delete_ads, name='ads_retrieve_update_delete'),

]
