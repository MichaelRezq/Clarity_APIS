from django.contrib import admin
from django.urls import path

from .views import CustomRegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/registration/', CustomRegisterView.as_view(), name='rest_register')]
