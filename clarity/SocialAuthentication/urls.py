
from django.contrib import admin
from django.urls import path,include,re_path

from .views import FacebookLogin, GoogleLogin,GithubLogin



urlpatterns = [
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('rest-auth/github/', GithubLogin.as_view(), name='google_login'),

]