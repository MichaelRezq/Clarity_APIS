from django.urls import  path,re_path
from allauth.account.views import ConfirmEmailView,AccountInactiveView,LogoutView
from rest_auth.registration.views import VerifyEmailView

# Password reset
from rest_auth.views import PasswordResetView, PasswordResetConfirmView,LoginView


from .views import CustomRegisterView ,UserListCreateView,UsertRetrieveUpdateDeleteView,UserDetailView, change_password

from .views import (
    FriendRequestListCreateAPIView,
    FriendRequestDetailAPIView,
    FriendRequestPendingAPIView,
    FriendRequestAcceptAPIView,
    FriendRequestDeclineAPIView,
)

urlpatterns = [
    path('userdetail/', UserDetailView.as_view(), name='userdetail'),
    path('users/', UserListCreateView.as_view(), name='user_list'),
    path('users/<int:pk>/', UsertRetrieveUpdateDeleteView.as_view(), name='user_details'),
    path('api/changepassword', change_password, name='change_password'),
    path('rest-auth/registration/', CustomRegisterView.as_view(), name='account_signup'),

    path(r'^confirm-email/(?P<key>[-:\w]+)/$',ConfirmEmailView.as_view(), name='account_confirm_email'),
    path('accounts/login/',LoginView.as_view(), name='account_login'),
    
    # path('rest-auth/registration/account-confirm-email/<str:key>/', VerifyEmailView.as_view(), name='account_confirm_email'),
    
    # # verfication for the email
    path('user/verify-email/',VerifyEmailView.as_view(),name='account_email_verification_sent'),
    path('user/account_email/',AccountInactiveView.as_view(),name='account_email'),
    path('rest-auth/logout/',LogoutView.as_view(),name='account_logout'),


    #        # Password reset
    # path('user/password/reset/',PasswordResetView.as_view(),name='rest_password_reset'),

    path('user/password/reset/confirm/<Uid>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

# for friends

    path('friendsrequest/', FriendRequestListCreateAPIView.as_view(), name='list_create'),
    path('friendsrequest/<int:pk>/', FriendRequestDetailAPIView.as_view(), name='detail'),
    path('friendsrequest/pending/', FriendRequestPendingAPIView.as_view(), name='pending'),
    path('friendsrequest/<int:pk>/accept/', FriendRequestAcceptAPIView.as_view(), name='accept'),
    path('friendsrequest/<int:pk>/decline/', FriendRequestDeclineAPIView.as_view(), name='decline'),
    ]