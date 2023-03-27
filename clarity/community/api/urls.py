from django.urls import include, path
from rest_framework import routers
from  .views import CommunityViewSet

router = routers.DefaultRouter()
router.register(r'communities', CommunityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
