"""clarity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path,include,re_path

from rest_framework.authtoken.views import obtain_auth_token
import posts.api.urls
import users.api.urls
import comments.api.urls
import community.api.urls
import problems.api.urls
import ads.api.urls
# import solutions.api.urls
import replays.api.urls
import chat.api.urls
import SocialAuthentication.urls
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
from django.conf.urls.static import static
import jobs.api.urls
import events.api.urls

# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'posts', PostListCreateView)
# router.register(r'comments', CommentListCreateView)
# router.register(r'problems', ProblemListCreateView)
# router.register(r'solutions', SolutionListCreateView)
# router.register(r'replies', CommentReplyList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(posts.api.urls)),
    path('', include(ads.api.urls)),
    path('', include(comments.api.urls)),
    path('', include(community.api.urls)),
    path('', include(problems.api.urls)),
    # path('', include(solutions.api.urls)),
    path('', include(chat.api.urls)),
    path('', include(replays.api.urls)),
    path('api_auth', include('rest_framework.urls')),
    path('api_token_auth', obtain_auth_token),
    path('rest-auth/', include('rest_auth.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include(users.api.urls)),
    path('', include(SocialAuthentication.urls)),
    path('',include(jobs.api.urls)),
    path('',include(events.api.urls)),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)