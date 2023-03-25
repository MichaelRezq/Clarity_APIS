
from django.contrib import admin
from django.urls import path,include,re_path

from .views import FacebookLogin, GoogleLogin



urlpatterns = [
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),

]