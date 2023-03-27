from django.contrib import admin
from django.urls import path
# from allauth.account.views import account_inactive

from .views import CustomRegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/registration/', CustomRegisterView.as_view(), name='rest_register'),
    # path('accounts/inactive/', account_inactive, name='account_inactive'),

    ]
