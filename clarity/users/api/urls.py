from django.contrib import admin
from django.urls import include, path
# from allauth.account.views import account_inactive
from rest_auth.registration.views import VerifyEmailView

from .views import CustomRegisterView ,UserListCreateView,UsertRetrieveUpdateDeleteView,UserDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userdetail/', UserDetailView.as_view(), name='userdetail'),
    path('users/', UserListCreateView.as_view(), name='user_list'),
    path('posts/<int:pk>/', UsertRetrieveUpdateDeleteView.as_view(), name='user_details'),
    path('rest-auth/registration/', CustomRegisterView.as_view(), name='rest_register'),
    path('rest-auth/registration/account-confirm-email/<str:key>/', VerifyEmailView.as_view(), name='account_confirm_email'),

    ]
